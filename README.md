# APB Reloaded Configuration Modifier

This Python script is designed to modify specific configuration files for the game **APB Reloaded**. It allows users to easily update settings related to frame rates and VSync directly from the script, ensuring a smoother gaming experience.

## Features

- **Administrator Permission Check**: The script automatically requests administrator permissions if not already granted.
- **Automatic Game Folder Detection**: It locates the APB Reloaded game folder within the Program Files directory.
- **Configuration File Modification**: It updates key settings in two configuration files:
  - `APBEngine.ini`
  - `BaseEngine.ini`
- **Customizable Settings**: Easily modify the frame rate and VSync settings by changing the values in the script.

## Settings Modified

The script modifies the following parameters:

- `MaxClientFrameRate`: Sets the maximum client frame rate (default: 999).
- `MaxSmoothedFrameRate`: Sets the maximum smoothed frame rate (default: 300).
- `UseVsync`: Enables or disables VSync (default: False).

## Requirements

- Python 3.x
- Administrative privileges on Windows

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/apb-reloaded-config-modifier.git
2. **Go to the script file**:
    ```bash
    cd apb-reloaded-config-modifier
3. **Run the script file**:
    ```bash
    python APB-auto-unlock-FPS.py