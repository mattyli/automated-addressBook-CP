import pyautogui as pg

def takeScreenShot():
    img = pg.screenshot()
    img.save(r'C:\downloads\screenshot.png')
