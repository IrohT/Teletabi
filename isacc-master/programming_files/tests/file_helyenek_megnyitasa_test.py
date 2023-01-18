import os
import subprocess


#________________________file megnyitó________________
def opener(path):
    
    browser_path= os.path.join(os.getenv('WINDIR'), 'explorer.exe') # file kezelő
    
    copy_kerdes = input("szeretnéd megnyitni a fájl helyét? i/n: ")
    if copy_kerdes == "i":
        path = os.path.basename(path)

        if os.path.isdir(path):
            subprocess.run([browser_path, path])
        else:
            subprocess.run([browser_path, '/select,', path])
    return None
#-----------------------------------------------------
