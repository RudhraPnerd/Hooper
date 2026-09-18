import os

SKIN_FILE = "src/skin.txt"
DEFAULT_SKIN = "hoop"

def read_skin():
    try:
        with open(SKIN_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return DEFAULT_SKIN

def save_skin(skin_name):
    os.makedirs(os.path.dirname(SKIN_FILE), exist_ok=True)
    with open(SKIN_FILE, "w") as f:
        f.write(skin_name)