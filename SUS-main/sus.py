import pyautogui as pg
import subprocess as sp
import time

pg.FAILSAFE = False

with open("sus.txt", "r", encoding="utf8") as f:
    with open("kaki.txt", "a", encoding="utf8") as o:
        for i in f.readlines():
            o.write(i)
            
        
    programName = "notepad.exe"
    fileName = "kaki.txt"
    sp.Popen([programName, fileName])
    time.sleep(2)
    pg.typewrite("u sussy baka UwU")
    pg.typewrite(["enter"])
    time.sleep(2)
    pg.typewrite("get poopied <3")
    pg.typewrite(["enter"])


    time.sleep(2)
    pg.click(0,1100)
    time.sleep(1)
    pg.click(25,1010)
    time.sleep(2)
    pg.moveTo(25,1000)
    #pg.click(25,960)


    