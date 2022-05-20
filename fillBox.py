import pyautogui as pg

def fillBox(tupleCoords, text):
    xCoord, yCoord = tupleCoords            # unpacking tuple
    pg.click(x=xCoord, y=yCoord)
    pg.typewrite(text)