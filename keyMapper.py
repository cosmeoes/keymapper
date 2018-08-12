import keyboard, configparser, subprocess, time
from os import path
config = configparser.ConfigParser()
config.read("keyMapper.conf")

def set_key_map(target, replacement):
    f = lambda event: keyboard.send(replacement) if event.event_type == keyboard.KEY_DOWN else None
    keyboard.hook_key(target, f, suppress=True)

if("Mapping" in config):
    for key, value in config['Mapping'].items():
        set_key_map(key, value)

for key, value in config['Hotkey'].items():
    print(key, value)
    keyboard.add_hotkey(key, lambda value=value: keyboard.write(value),  suppress=True)


def exec_command(value, dir):
    print("doing %s in %s" % (value, dir))
    args = value.split(',')
    for i, arg in enumerate(args):
        args[i] = arg.strip()
    subprocess.run(args, cwd=dir, shell=True)

for key, value in config['Scripts'].items():
    args = value.split(",")
    dir = None
    if(path.dirname(args[0]) and path.isdir(path.dirname(args[0]))):
        dir = path.dirname(args[0])
    keyboard.add_hotkey(key, exec_command, args=[value, dir], suppress=True)


while(True):
    time.sleep(0.1)
