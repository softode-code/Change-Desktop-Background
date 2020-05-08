import os
import random
import ctypes
import schedule
import time

Path = "E:\\Wallpapers\\"
SPI_SETDESKWALLPAPER = 20

def changeBG():
    path = Path+random.choice(os.listdir(Path))
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,path,3)

schedule.every().hours.do(changeBG)

f = open('pid.txt','w+')
pid = os.getpid()
f.write(str(pid))
f.close()

while True:
    schedule.run_pending()
    time.sleep(1)