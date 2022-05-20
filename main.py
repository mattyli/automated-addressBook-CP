# import statements and constants
from pandas import read_excel
import pyautogui as pg
import pandas as pd
import numpy as np
import pathlib as pl
from fillBox import fillBox
import sys

# dictionary to store the provinces
provinces = {"ON" : "Ontario", "AB" : "Alberta", "MB" : "Manitoba", "PE" : "Prince Edward Island", "NL" : "Newfoundland and Labrador", "BC" : "British Columbia",
             "YT" : "Yukon", "NS" : "Nova Scotia", "QC" : "Quebec", "NU" : "Nunavut", "SK" : "Saskatchewan", "NB" : "New Brunswick", "NT" : "Northwest Territories"
}
ID, CITY, ADDRESS, POSTALCODE, PROVINCE, EMAIL = 0,4,5,6,7          # correspond to indices of current row

CUSTOMERNAME    = "COSMETIC MANAGER"            # constant field
COMPANY         = "SDM-SHOPPERS DRUG MART"      # constant field

# Creating the dataframe
try:
    #rawPath = str(input("Please paste the file path to the customer data: "))
    #goodPath = rawPath.replace("\\", "/")              # fixing the path
    customerDF = read_excel("SDMdata.xlsx")             # give filepath to the datasheet
    rowNum = len(customerDF.index)      # getting the number of data entries for iterating
except:
    print("File not found/ doesn't exist/ something is wrong")
    sys.exit()                          # quit the program

# getting the Field coordinates
# Fields that need to be filled in/ are drop downs
idField = pg.locateCenterOnScreen()
nameField = pg.locateCenterOnScreen()
companyField = pg.locateCenterOnScreen()
cityField = pg.locateCenterOnScreen()            
addressField = pg.locateCenterOnScreen()
postalField = pg.locateCenterOnScreen()
canadaField = pg.locateCenterOnScreen()
provinceField = pg.locateCenterOnScreen()
emailField = pg.locateCenterOnScreen()

# Buttons that will need to be pressed
saveBtn = pg.locateCenterOnScreen("images/saveBtn.png")                     # save customer
newCustBtn = pg.locateCenterOnScreen("images/newCustBtn.png")               # add new customer
bookBtn = pg.locateCenterOnScreen("images/addressBookBtn.png")

# driver code to populate the address book
for row in range(rowNum):
    currentRow = list(customerDF.loc[row])

    fillBox(idField, str(currentRow[ID]))
    fillBox(nameField, CUSTOMERNAME)
    fillBox(companyField, COMPANY)

    fillBox(provinceField, provinces[str(currentRow[PROVINCE])])


