import os
import random
import ctypes
import schedule
import time
from datetime import datetime

Path = "E:\\Wallpapers\\"
SPI_SETDESKWALLPAPER = 20

def changeBG():
    random.seed(datetime.now())
    path = Path+random.choice(os.listdir(Path))
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,path,3)

schedule.every(1).hours.do(changeBG)

f = open('Change Background PID.txt','w+')
pid = os.getpid()
f.write(str(pid))
f.close()

while True:
    schedule.run_pending()
    time.sleep(1)