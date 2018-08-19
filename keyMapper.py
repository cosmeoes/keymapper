import keyboard
from configManager import load_config
from pystray import MenuItem as item
import pystray
from PIL import Image
CONFIG_PATH = "keyMapper.conf"

load_config(CONFIG_PATH)


def reload_config():
    keyboard.unhook_all()
    load_config(CONFIG_PATH)
    pass

image = Image.open("img/keyboard.png")
menu = [item('Reload Config',lambda: reload_config()), item('Exit', lambda: icon.stop())]
icon = pystray.Icon("keyMaper", image, "keyMaper", menu)

def setup(icon):
    icon.visible = True

icon.run(setup)
