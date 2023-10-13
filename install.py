#!/usr/bin/env python3

import platform
from os import environ
from shutil import copy

platform = platform.system()

def copyToPath(path):
    print(f"Installing to {path}")

    try:
        copy('mrsocko', path)
    except PermissionError:
        print('Unable to copy to path due to inadequate permissions. Try installing as root!')

def installNIX():
    paths = environ['PATH'].split(':')
    if '/usr/local/bin' in paths:
        print('/usr/local/bin found in path.')
        copyToPath('/usr/local/bin')
    elif '/opt/bin' in paths:
        print('/opt/bin found in path.')
        copyToPath('/opt/bin')
    elif '/opt' in paths:
        print('/opt found in path.')
        copyToPath('/opt')
    elif '/usr/bin' in paths:
        print('/opt found in path.')
        copyToPath('/usr/bin')


def installBSD():
    pass

def installWindows():
    pass

def installOSX():
    pass

if platform == 'Linux':
    installNIX()
elif platform == 'Windows':
    installWindows()
elif platform == 'BSD':
    installNIX()
elif platform == 'OSX':
    installOSX()
