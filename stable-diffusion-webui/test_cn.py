import sys
import traceback

try:
    import cv2
    print("cv2 imported successfully. Version:", cv2.__version__)
except Exception as e:
    print("Failed to import cv2:")
    traceback.print_exc()

try:
    sys.path.append("extensions/sd-webui-controlnet")
    from scripts import controlnet
    print("ControlNet imported successfully.")
except Exception as e:
    print("Failed to import controlnet:")
    traceback.print_exc()
