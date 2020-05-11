import os
import ctypes
import sys
import random

Path = "E:\\Wallpapers\\"

if len(sys.argv) ==2:
    if sys.argv[1] == '--shuffle':
        path = Path+random.choice(os.listdir(Path))
        ctypes.windll.user32.SystemParametersInfoW(20 ,0,path,3)
else:
    print ('Wrong Parameters')
