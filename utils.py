import keyboard, subprocess
from os import path
import logging

logger = logging.getLogger();

def set_key_map(target, replacement):
    if len(keyboard.key_to_scan_codes(target, error_if_missing=False)) > 0 and len(keyboard.key_to_scan_codes(replacement, error_if_missing=False) > 0):
        logger.info("mapping %s to %s" % (target, value))
        f = lambda event: keyboard.send(replacement) if event.event_type == keyboard.KEY_DOWN else None
        return keyboard.hook_key(target, f, suppress=True)
    else:
        logger.warning("Could not map '%s' to '%s', bad config" % (target, replacement))


def set_hotkey(target, text_to_write):
    logger.info("Setting hotkey '%s' to write '%s'" % (target, text_to_write))
    return keyboard.add_hotkey(target, lambda text_to_write=text_to_write: keyboard.write(text_to_write),  suppress=True)

def set_script(target, action):
    args = action.split(",")
    dir = None
    if(path.dirname(args[0]) and path.isdir(path.dirname(args[0]))):
        dir = path.dirname(args[0])
        logger.info("Script path for %s set to %s" % (args[0], dir))
    return keyboard.add_hotkey(target, exec_command, args=[action, dir], suppress=True)


def exec_command(value, dir):
    print("doing %s in %s" % (value, dir))
    args = value.split(',')
    for i, arg in enumerate(args):
        args[i] = arg.strip()
    subprocess.run(args, cwd=dir, shell=True)
