import time
import ctypes

def ScreenOFF():
    """
    Function to turn off the screen.
    """
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)

def ScreenON():
    """
    Function to turn on the screen.
    """
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)

ScreenOFF()
time.sleep(5)
ScreenON()