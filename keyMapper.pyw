import keyboard, logging, pystray, sys, os
from configManager import load_config
from pystray import MenuItem as item
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='A python script to map keys to scripts other keys or typing')
parser.add_argument('config', nargs="?", default="keyMapper.conf",
                   help='sets the configuration file location (default is ./keyMapper.conf)')
args = parser.parse_args(sys.argv[1:])
CONFIG_PATH = args.config

LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"
logging.basicConfig(filename = 'keyMapper.log', level = logging.INFO, format = LOG_FORMAT)
logger = logging.getLogger()
logger.info("Loading config from %s" % (CONFIG_PATH))

if not os.path.isfile(CONFIG_PATH):
    logger.error("Can't find configuration file in: %s, exiting" % (CONFIG_PATH))
    exit();
load_config(CONFIG_PATH)


def reload_config():
    keyboard.unhook_all()
    logger.info("Reloading config from %s" % (CONFIG_PATH))
    load_config(CONFIG_PATH)

def exit_program():
    logger.info("Stoping keyMapper, bye")
    icon.stop()

image = Image.open("img/keyboard.png")
menu = [item('Reload Config',lambda: reload_config()), item('Exit', lambda: exit_program())]
icon = pystray.Icon("keyMapper", image, "keyMapper", menu)

def setup(icon):
    icon.visible = True

logger.info("Startig icon tray")
icon.run(setup)
