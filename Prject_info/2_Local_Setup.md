# How to Run this Project on Your Local Computer

Because you are using Windows, setting up the Stable Diffusion WebUI locally involves a few strict prerequisites to ensure everything runs smoothly.

## Prerequisites
1. **Python 3.10.6:** This exact version is heavily recommended. Newer versions of Python often cause compatibility issues with PyTorch and other deep learning dependencies. 
   - When installing Python, **you must check the box that says "Add Python to PATH"** before clicking Install.
2. **Git:** Used to download and update the repository and its extensions.
3. **GPU (Graphics Card):** An NVIDIA GPU with at least 4GB to 8GB of VRAM is highly recommended. It is possible to run it on CPU or AMD GPUs, but it requires different configurations and is significantly slower.

## First-Time Setup & Running
1. Open your File Explorer and navigate to the project directory: `c:\Users\aryan\OneDrive\Desktop\Image gen env\stable-diffusion-webui`
2. Scroll down until you find the file named `webui-user.bat`.
3. **Double-click `webui-user.bat`** to run it.
4. A black terminal window (Command Prompt) will open. On its first run, it will take a long time (potentially 15-30 minutes depending on your internet speed). It is automatically downloading PyTorch, the Gradio web server files, and a default base model (usually about 4GB).
5. Do not close this terminal window.

## Accessing the Interface
Once the terminal finishes installing everything, you will see a message that says:
`Running on local URL:  http://127.0.0.1:7860`

1. Open your favorite web browser (Chrome, Edge, Firefox, etc.).
2. Type `http://127.0.0.1:7860` into the address bar and hit Enter.
3. The WebUI will load, and you can start generating images!

## Stopping the Project
To stop the server, simply click on the terminal window and press `Ctrl + C`, or just close the terminal window completely.

## Future Runs
You don't need to install everything again. Every time you want to start the project, just double-click `webui-user.bat`. It will boot up much faster.
