import pyautogui as pg
from soupsieve import match
from generalTypewrite import generalTypewrite

def fillDropdown(tupleCoords, item, nonUniqueChar="N"):
    item = str(item).upper()        # item is a string, just to make sure
    fc = item[0]
    xC, yC = tupleCoords
    pg.click(x=xC,y=yC)             # moving to the box
    if fc != nonUniqueChar.upper():
        pg.typewrite(fc)            # will not work
        pg.press('enter')
        return
    else:
        # is item that begins with N (there are 5)
        # handle the non unique, using match in python 3.10.4

        match fc:
            case "NWT":
                pg.locateCenterOnScreen() # find the NWT box
                pg.click()
            case "NU":
                pg.locateCenterOnScreen()
                pg.click()
            case "NL":
                pg.locateCenterOnScreen()
                pg.click()
            case "NB":
                pg.locateCenterOnScreen()
                pg.click()
            case "NS":
                pg.locateCenterOnScreen()
                pg.click()
        return

"""
    this is a general function that can be used to fill a dropdown selector using some pyautogui functions.
    EST 2.0 (which this was designed for) doesn't allow you to cycle through options that start with the same
    letter by pressing that letter, thus I had to design a unique solution for that using the scroll function
    of pyautogui.
"""