# Image Generation Environment

A complete Stable Diffusion WebUI setup for generating high-quality images using AI. This repository contains a fully configured Stable Diffusion WebUI environment ready for image generation tasks.

## 📋 Overview

This project includes the [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) - a powerful web interface for Stable Diffusion, implemented using the Gradio library. It provides an intuitive interface for text-to-image and image-to-image generation with advanced features and customization options.

## ✨ Features

- **Text-to-Image (txt2img)**: Generate images from text prompts
- **Image-to-Image (img2img)**: Transform existing images using AI
- **Inpainting & Outpainting**: Edit specific parts of images or extend them
- **Upscaling**: Enhance image resolution using various AI models (GFPGAN, CodeFormer, RealESRGAN, ESRGAN, SwinIR, LDSR)
- **Face Restoration**: Fix faces in generated images
- **Prompt Engineering**: Advanced prompt features including attention weighting, negative prompts, and prompt styles
- **Checkpoint Management**: Easy loading and switching between different Stable Diffusion models
- **LoRA & Hypernetworks**: Support for fine-tuned models and style modifiers
- **Textual Inversion**: Train and use custom embeddings
- **Batch Processing**: Process multiple images at once
- **API Support**: RESTful API for programmatic access
- **Custom Scripts**: Extensible with community-contributed scripts

## 🚀 Quick Start

### Prerequisites

- **Python 3.10.6** (Newer versions may not be fully supported)
- **Git** for cloning repositories
- **NVIDIA GPU** (recommended) with CUDA support, or CPU/AMD GPU support
- At least **4GB VRAM** (2GB may work with optimizations)

### Installation on Windows

1. **Install Python 3.10.6**
   - Download from [python.org](https://www.python.org/downloads/release/python-3106/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install Git**
   - Download from [git-scm.com](https://git-scm.com/download/win)

3. **Run the WebUI**
   ```bash
   cd stable-diffusion-webui
   webui-user.bat
   ```

   The first run will automatically:
   - Install all required dependencies
   - Download necessary models
   - Set up the environment

4. **Access the Interface**
   - Open your browser and navigate to `http://127.0.0.1:7860`
   - The interface will be ready to use!

### Installation on Linux

1. **Install Dependencies**
   ```bash
   # Debian-based (Ubuntu, etc.)
   sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
   
   # Red Hat-based
   sudo dnf install wget git python3 gperftools-libs libglvnd-glx
   ```

2. **Run the WebUI**
   ```bash
   cd stable-diffusion-webui
   bash webui.sh
   ```

### Installation on macOS (Apple Silicon)

See the [official installation guide](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon) for detailed instructions.

## 📁 Project Structure

```
Image-gen-env/
├── stable-diffusion-webui/    # Main WebUI application
│   ├── models/                 # Model files (checkpoints, LoRA, VAE, etc.)
│   ├── outputs/                # Generated images
│   ├── extensions/             # Custom extensions
│   ├── embeddings/             # Textual inversion embeddings
│   ├── scripts/                # Custom scripts
│   └── ...
└── README.md                   # This file
```

## 🎨 Usage

### Basic Text-to-Image Generation

1. Open the WebUI in your browser
2. Navigate to the **txt2img** tab
3. Enter your prompt in the text field
4. Adjust settings (sampling method, steps, CFG scale, etc.)
5. Click **Generate**

### Example Prompts

- `a beautiful landscape, mountains, sunset, highly detailed, 4k`
- `portrait of a cyberpunk character, neon lights, futuristic, artstation`
- `cute cat playing with yarn, soft lighting, photorealistic`

### Advanced Features

- **Negative Prompts**: Specify what you don't want in the image
- **Attention Weighting**: Use `(keyword)` for emphasis or `[keyword]` for de-emphasis
- **Prompt Styles**: Save and reuse common prompt patterns
- **Checkpoint Merger**: Combine multiple models
- **X/Y/Z Plot**: Compare different parameter combinations

## 🔧 Configuration

### Settings

Access settings via the **Settings** tab in the WebUI interface. Key settings include:

- Model selection and management
- VAE selection
- Sampling parameters
- UI customization
- Extensions management

### Command Line Arguments

Edit `webui-user.bat` (Windows) or `webui-user.sh` (Linux) to add command line arguments:

```bash
# Example: Enable xformers for faster generation
set COMMANDLINE_ARGS=--xformers

# Example: Change port
set COMMANDLINE_ARGS=--port 7861
```

Common arguments:
- `--xformers`: Enable xformers for faster generation (NVIDIA GPUs)
- `--api`: Enable API mode
- `--listen`: Allow network access
- `--port`: Change the port number

## 📦 Model Management

### Adding Models

1. **Stable Diffusion Checkpoints**: Place `.ckpt` or `.safetensors` files in `stable-diffusion-webui/models/Stable-diffusion/`
2. **VAE Models**: Place in `stable-diffusion-webui/models/VAE/`
3. **LoRA Models**: Place in `stable-diffusion-webui/models/Lora/`
4. **Embeddings**: Place in `stable-diffusion-webui/embeddings/`

### Recommended Models

- **Base Models**: SD 1.5, SD 2.1, SDXL
- **VAE**: vae-ft-mse-840000-ema-pruned.safetensors
- **Upscalers**: RealESRGAN models

## 🔌 Extensions

Install extensions from the **Extensions** tab:

1. Go to **Extensions** → **Available**
2. Click **Load from** to refresh the list
3. Find and install desired extensions
4. Restart the WebUI

Popular extensions:
- ControlNet
- Additional Networks
- Image Browser
- Prompt All-in-One

## 🐛 Troubleshooting

### Common Issues

**Out of Memory (OOM) Errors**
- Reduce image resolution
- Enable `--lowvram` or `--medvram` flags
- Use `--xformers` for better memory efficiency

**Slow Generation**
- Enable `--xformers` (NVIDIA GPUs)
- Reduce image resolution
- Use fewer sampling steps
- Check GPU drivers are up to date

**Models Not Loading**
- Ensure model files are in the correct directory
- Check file format (`.ckpt`, `.safetensors`)
- Verify model compatibility with your WebUI version

## 📚 Resources

- [Official Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki)
- [Feature Showcase](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features)
- [Installation Guides](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs)
- [API Documentation](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API)

## 🤝 Contributing

This repository is based on the [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) project. For contributing to the original project, see their [Contributing Guide](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Contributing).

## 📄 License

This project uses the same license as the original Stable Diffusion WebUI. See `stable-diffusion-webui/LICENSE.txt` for details.

## 🙏 Credits

- **Stable Diffusion WebUI**: [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- **Stable Diffusion**: Stability AI
- **Gradio**: For the web interface framework
- All the contributors and extension developers in the community

## ⚠️ Important Notes

- **Model Files**: Large model files (checkpoints, VAE, etc.) are not included in this repository due to size limitations. You'll need to download them separately.
- **GPU Requirements**: While CPU generation is possible, it's extremely slow. A GPU is highly recommended.
- **Legal Compliance**: Ensure you have proper licenses for any models you use and comply with their terms of service.

## 📞 Support

For issues and questions:
- Check the [Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki)
- Visit the [Discussions](https://github.com/AUTOMATIC1111/stable-diffusion-webui/discussions)
- Review existing [Issues](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues)

---

**Happy Generating! 🎨✨**

