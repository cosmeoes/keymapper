import keyboard, subprocess
from os import path

def set_key_map(target, replacement):
    f = lambda event: keyboard.send(replacement) if event.event_type == keyboard.KEY_DOWN else None
    return keyboard.hook_key(target, f, suppress=True)

def set_hotkey(target, text_to_write):
     return keyboard.add_hotkey(target, lambda text_to_write=text_to_write: keyboard.write(text_to_write),  suppress=True)

def set_script(target, action):
    args = action.split(",")
    dir = None
    if(path.dirname(args[0]) and path.isdir(path.dirname(args[0]))):
        dir = path.dirname(args[0])
    return keyboard.add_hotkey(target, exec_command, args=[action, dir], suppress=True)

def exec_command(value, dir):
    print("doing %s in %s" % (value, dir))
    args = value.split(',')
    for i, arg in enumerate(args):
        args[i] = arg.strip()
    subprocess.run(args, cwd=dir, shell=True)
