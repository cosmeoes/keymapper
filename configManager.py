import configparser
from utils import set_key_map, set_script, set_hotkey


def load_mappings(mapping_dict):
    for key, value in mapping_dict.items():
        set_key_map(key, value)

def load_hotkeys(hotkey_dict):
    for key, value in hotkey_dict.items():
        print(key, value)
        set_hotkey(key, value)

def load_scripts(scripts_dict):
    for key, value in scripts_dict.items():
        set_script(key, value)

def load_config(file_path):
    config = configparser.ConfigParser()
    config.read("keyMapper.conf") #TODO: change this to file_path
    if("Mapping" in config):
        load_mappings(config['Mapping'])
    if("Hotkey" in config):
        load_hotkeys(config['Hotkey'])
    if("Scripts" in config):
        load_scripts(config['Scripts'])
