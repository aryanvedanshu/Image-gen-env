import os
import time
import base64
from io import BytesIO
import modules.scripts as scripts
import modules.shared as shared

# Cost mapping per hour (On-Demand pricing)
PRICING_PER_HOUR = {
    "AWS EC2 (g5.2xlarge - A10G)": 1.212,
    "GCP (g2-standard-4 - L4)": 0.562,
    "Azure (Standard_NV6ads_A10_v5)": 0.825,
    "RunPod (RTX 4090 Secure Cloud)": 0.74
}

def img_to_base64(img):
    if img is None:
        return ""
    try:
        buffered = BytesIO()
        # Convert to RGB to avoid issues with saving RGBA as JPEG
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(buffered, format="JPEG", quality=85)
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    except Exception as e:
        print(f"[Business Logger] Error converting image to base64: {e}")
        return ""

class BusinessLoggerScript(scripts.Script):
    def title(self):
        return "Business Cost & Generation Logger"

    def show(self, is_img2img):
        # Return AlwaysVisible so it runs unconditionally in the background
        return scripts.AlwaysVisible

    def process(self, p, *args, **kwargs):
        # Capture the start time
        self.start_time = time.time()
        return

    def postprocess(self, p, processed, *args):
        end_time = time.time()
        duration = end_time - getattr(self, 'start_time', end_time)

        # Safety check: ensure we actually generated something
        if not processed.images or len(processed.images) == 0:
            return

        # Extract images
        original_img = None
        if hasattr(p, 'init_images') and p.init_images and len(p.init_images) > 0:
            original_img = p.init_images[0]
            
        mask_img = None
        if hasattr(p, 'image_mask') and p.image_mask:
            mask_img = p.image_mask
            
        # The main generated output image
        output_img = processed.images[0]
        
        # Extract prompt
        prompt = p.prompt if p.prompt else "No prompt provided"

        # Determine output directory
        outpath = p.outpath_samples if hasattr(p, 'outpath_samples') and p.outpath_samples else "outputs"
        os.makedirs(outpath, exist_ok=True)
        
        timestamp = int(time.time())
        report_filename = os.path.join(outpath, f"business_report_{timestamp}.html")

        # Build Cost HTML
        cost_html = "<ul>"
        for name, hourly_rate in PRICING_PER_HOUR.items():
            cost_per_sec = hourly_rate / 3600.0
            total_cost = cost_per_sec * duration
            # Format to 6 decimal places for readability on micro-transactions
            cost_html += f"<li><b>{name}:</b> ${total_cost:.6f}</li>"
        cost_html += "</ul>"

        # Convert images to Base64 strings for standalone HTML
        orig_b64 = img_to_base64(original_img)
        mask_b64 = img_to_base64(mask_img)
        out_b64 = img_to_base64(output_img)
        
        # Build Image blocks
        img_html = ""
        if orig_b64:
            img_html += f"<div><h3>Original Input</h3><img src='data:image/jpeg;base64,{orig_b64}' style='max-width:350px;'/></div>"
        if mask_b64:
            img_html += f"<div><h3>Mask Used</h3><img src='data:image/jpeg;base64,{mask_b64}' style='max-width:350px;'/></div>"
        if out_b64:
            img_html += f"<div><h3>Final Generation</h3><img src='data:image/jpeg;base64,{out_b64}' style='max-width:350px;'/></div>"

        # Assemble final HTML
        html_content = f"""
        <html>
        <head>
            <title>Business Generation Report</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; background-color: #f8f9fa; color: #212529; }}
                h1 {{ color: #343a40; border-bottom: 2px solid #dee2e6; padding-bottom: 10px; }}
                h3 {{ color: #495057; }}
                .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); max-width: 1200px; margin: 0 auto; }}
                .images {{ display: flex; gap: 20px; flex-wrap: wrap; margin-top: 30px; }}
                .images div {{ border: 1px solid #e9ecef; padding: 15px; border-radius: 8px; background: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }}
                .info-box {{ margin-top: 20px; padding: 20px; background: #e3f2fd; border-left: 6px solid #2196f3; border-radius: 4px; }}
                .cost-box {{ margin-top: 20px; padding: 20px; background: #e8f5e9; border-left: 6px solid #4caf50; border-radius: 4px; }}
                p {{ line-height: 1.6; font-size: 1.05em; }}
                ul {{ font-size: 1.05em; line-height: 1.8; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>AI Image Generation Report</h1>
                <p><b>Timestamp:</b> {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}</p>
                
                <div class="info-box">
                    <h3>Generation Metadata</h3>
                    <p><b>Total Execution Time:</b> {duration:.2f} seconds</p>
                    <p><b>Prompt:</b> {prompt}</p>
                </div>

                <div class="cost-box">
                    <h3>Estimated Production Server Costs</h3>
                    <p><i>Calculated based on standard On-Demand hourly pricing. Spot/Preemptible instances would be 60-70% cheaper.</i></p>
                    {cost_html}
                </div>

                <div class="images">
                    {img_html}
                </div>
            </div>
        </body>
        </html>
        """

        # Save HTML file
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"[Business Logger] Successfully saved HTML report to: {report_filename}")

