import pyautogui as pg

def generalTypewrite(msg, times=1):
    for press in range(times):
        pg.typewrite(msg)

# helper function, essentially wrapping the pyautogui.typewrite() method