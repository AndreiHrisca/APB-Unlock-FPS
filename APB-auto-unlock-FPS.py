import os
import ctypes
import sys

# Function to request administrator permissions
def request_admin():
    """Request admin permissions for the script."""
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        # Restart the script with administrator permissions
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        return False

# Name of the game folder and the configuration files
GAME_FOLDER_NAME = "APB Reloaded"
APBENGINE_FILE = "APBEngine.ini"
BASEENGINE_FILE = "BaseEngine.ini"

# Function to find the game folder
def find_game_folder():
    """Locate the game folder in Program Files."""
    program_files = [os.environ.get("ProgramFiles(x86)"), os.environ.get("ProgramFiles")]
    for folder in program_files:
        if folder:
            game_folder_path = os.path.join(folder, "GamersFirst", GAME_FOLDER_NAME)
            if os.path.exists(game_folder_path):
                return game_folder_path
    return None

# Check for administrator permissions
if not request_admin():
    print("Administrator permissions are required to run this script.")
    sys.exit()

# Find the game folder
game_folder = find_game_folder()

if game_folder is None:
    print("Game folder not found.")
    sys.exit()

# Define paths to the configuration files
apbengine_path = os.path.join(game_folder, "APBGame", "Config", APBENGINE_FILE)
baseengine_path = os.path.join(game_folder, "Engine", "Config", BASEENGINE_FILE)

# New values to apply to the configuration files
NEW_SETTINGS = {
    "APBEngine.ini": {
        "MaxClientFrameRate": "MaxClientFrameRate=999",
        "MaxSmoothedFrameRate": "MaxSmoothedFrameRate=300",
        "UseVsync": "UseVsync=False",
    },
    "BaseEngine.ini": {
        "MaxClientFrameRate": "MaxClientFrameRate=999",
        "MaxSmoothedFrameRate": "MaxSmoothedFrameRate=300",
    },
}

# Function to modify a configuration file
def modify_file(file_path, settings):
    """Modify the specified configuration file with new settings."""
    if not os.path.exists(file_path):
        print(f"The file is not found at: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                # Update the line if it matches any setting key
                for key, value in settings.items():
                    if key in line:
                        line = value + "\n"  # Replace the line with the new value
                file.write(line)

        print(f"The file {file_path} has been updated.")
    except Exception as e:
        print(f"An error occurred while modifying {file_path}: {e}")

# Execute the modification for each configuration file
for filename, settings in NEW_SETTINGS.items():
    file_path = os.path.join(game_folder, "APBGame", "Config" if "APBEngine" in filename else "Engine", filename)
    modify_file(file_path, settings)