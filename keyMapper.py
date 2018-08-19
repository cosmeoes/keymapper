import keyboard, configparser, subprocess, time, sys
from os import path
from configManager import load_config

load_config("keyMapper.conf")


while(True):
    time.sleep(10000)
