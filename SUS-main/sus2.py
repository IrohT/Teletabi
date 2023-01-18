import pyautogui as pg
import time
import subprocess as sp
 
def delete_for_everyone():
    
    pg.typewrite("hello")
    pg.typewrite(["enter"])
    time.sleep(2)
    pg.click(1621, 896)
    pg.click(1621, 896)
     
    # time.sleep(1)
    pg.click(1693, 859)
     
    # time.sleep(1)
    pg.click(1014, 669)
     
    # time.sleep(1)
    pg.click(1111, 605)

    

programName = "notepad.exe"
fileName = "kaki.txt"
sp.Popen([programName, fileName])
time.sleep(2)
pg.typewrite("hello")
pg.typewrite(["enter"])


