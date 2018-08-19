# keyMapper
A python script to map keys to scripts other keys or typing

## Configuration
The configurations can be found and edited in the keyMapper.conf file.
This file is separated in three sections mapping, hotkey and scripts.

#### Mapping
Here you put keys you want to bind to other keys, for example, if you want o bind the "a" key to write a "b"
when you press it you would do:
```
[Mapping]
a = b
```
NOTE: this configurations only accept a key binding to another key, you can not bind a key to two keys for example:
```
[Mapping]
a = bb # THIS IS WRONG and will produce an error,
aa = b # THIS IS also WRONG and will produce an error.
```

#### Hotkey
Here you can set up multiple key combinations and more complex key presses, for example, if you'd want to write "python is fun"
when you press "ctrl + a" and then "p" you would write:
```
[Hotkey]
ctrl + a, p = python is fun
```
NOTE: this are the modifiers you can use:
'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift', 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows', 'shift', 'windows'

#### Scripts
Here you can set up scripts or programs to execute when you press a combination of keys, this follows the same format as the hotkey section.
First you write the keys you what to bind to the script or program and then you write the path to the script or program.
You can also use shell commands instead of the path of your script.
for example if you want to start cmd prompt when you press "windos+enter" you would do it like this:
```
[Scripts]
windows+enter = start
```
you can also pass arguments your scripts with "," after the script's or program's path
for example if you want to launch a python script located at "C:\script.py" and wanted to pass the arguments "argument1" and "argument2" when
you press "ctrl+l, space" you would write:
```
[Scripts]
ctrl+l, space = C:\script.py, argument1, argument2
```

## Dependencies

 - [keyboard](https://github.com/boppreh/keyboard)

 - [Pillow](https://github.com/python-pillow/Pillow)

 - [pystray](https://github.com/moses-palmer/pystray)

## Other Credits
Icon made by [Dave Gandy](https://www.flaticon.com/authors/dave-gandy) from www.flaticon.com
