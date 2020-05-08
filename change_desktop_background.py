import os
import random
import ctypes

Path = "E:\\Wallpapers\\"
SPI_SETDESKWALLPAPER = 20


def changeBG(path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,path,3)

changeBG(Path+random.choice(os.listdir(Path)))