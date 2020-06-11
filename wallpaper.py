import os
import ctypes
import sys
import random
from datetime import datetime

Path = "E:\\Wallpapers\\"

random.seed(datetime.now())
path = Path+random.choice(os.listdir(Path))
ctypes.windll.user32.SystemParametersInfoW(20 ,0,path,3)