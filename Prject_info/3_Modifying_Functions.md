# How to Modify the Functions of this Project

The Stable Diffusion WebUI is highly modular and designed to be easily modified or extended without having to rewrite the core source code. 

## 1. Adding Pre-built Functions (Extensions)
The easiest way to modify the UI and add functions (like ControlNet, image browsers, or custom prompt generators) is through **Extensions**.
1. Open the WebUI in your browser.
2. Go to the **Extensions** tab at the top.
3. Click on the **Available** sub-tab and click the orange **Load from:** button.
4. Search for the extension you want, click Install, and then go to the **Installed** tab to Apply and Restart the UI.

## 2. Modifying the Interface & Logic via Code
If you want to write your own custom functions or change how things work, you have two main approaches:

### Custom Scripts (Python)
You can write custom Python scripts to modify how generation happens or add new UI elements to the bottom of the generation tab.
- **Location:** Place your Python scripts in `stable-diffusion-webui/scripts/`.
- Scripts written here use Gradio to add interface elements and hook into the core generation loop.

### Custom Extensions
If you want to build a more complex modification (like adding a completely new tab to the top of the screen), you should create an extension.
- **Location:** Create a new folder inside `stable-diffusion-webui/extensions/`.
- Inside that folder, you can place a `scripts/` folder for your Python code, and a `javascript/` or `css/` folder for frontend modifications.
- **How it works:** The WebUI looks through all folders in the `extensions/` directory on startup and injects their Python, JS, and CSS files into the main application.

## 3. Modifying Startup Arguments
You can change how the server runs (e.g., making it accessible to other devices on your Wi-Fi, or optimizing VRAM usage) by editing the `webui-user.bat` file.
1. Right-click `webui-user.bat` and select **Edit** (or open it in Notepad).
2. Find the line that says `set COMMANDLINE_ARGS=`.
3. Add arguments here. For example:
   - `set COMMANDLINE_ARGS=--xformers --medvram` (to optimize memory usage and speed on NVIDIA cards).
   - `set COMMANDLINE_ARGS=--listen` (to allow access from other devices on your local network).

## 4. Editing the Core Source Code
If you absolutely must change the core behavior:
- The core Gradio interface is defined in `stable-diffusion-webui/modules/ui.py`.
- The generation logic is handled in `stable-diffusion-webui/modules/processing.py`.
- *Warning:* Editing core files directly can cause conflicts when updating the repository using `git pull`. It's always highly recommended to use Extensions or Scripts instead.
