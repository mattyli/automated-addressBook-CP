import pyautogui as pg
from generalTypewrite import generalTypewrite

def chooseProvince(prov):
    prov = str(prov).upper()        # prov is a string, just to make sure
    fc = prov[0]
    if fc != "N":
        # province that does not begin with N
        pg.typewrite(fc)
    else:
        # is province that begins with N (there are 5)
        return

