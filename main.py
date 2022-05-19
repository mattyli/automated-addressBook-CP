# import statements and constants
from pandas import read_excel
import pyautogui
import pandas as pd
import numpy as np
import pathlib as pl

# dictionary to store the provinces
provinces = {"ON" : "Ontario", "AB" : "Alberta", "MB" : "Manitoba", "PE" : "Prince Edward Island", "NL" : "Newfoundland and Labrador", "BC" : "British Columbia",
             "YT" : "Yukon", "NS" : "Nova Scotia", "QC" : "Quebec", "NU" : "Nunavut", "SK" : "Saskatchewan", "NB" : "New Brunswick", "NT" : "Northwest Territories"
}
ID, City, Address, PostalCode, Province, Email = 0,3,4,5,6

customerName    = "COSMETIC MANAGER"            # constant field
company         = "SDM-SHOPPERS DRUG MART"      # constant field

# Creating the dataframe
try:
    #rawPath = str(input("Please paste the file path to the customer data: "))
    #goodPath = rawPath.replace("\\", "/")       # fixing the path
    customerDF = read_excel("SDMdata.xlsx")            # give filepath to the datasheet
    rowNum = len(customerDF.index)      # getting the number of data entries for iterating
except:
    print("File not found/ doesn't exist")

# getting the Field coordinates
# Fields that need to be filled in/ are drop downs
idField = pyautogui.locateCenterOnScreen()
nameField = pyautogui.locateCenterOnScreen()
companyField = pyautogui.locateCenterOnScreen()
cityField = pyautogui.locateCenterOnScreen()            
addressField = pyautogui.locateCenterOnScreen()
postalField = pyautogui.locateCenterOnScreen()
canadaField = pyautogui.locateCenterOnScreen()
provinceField = pyautogui.locateCenterOnScreen()
emailField = pyautogui.locateCenterOnScreen()

# Buttons that will need to be pressed
saveBtn = pyautogui.locateCenterOnScreen()              # save customer
addBtn = pyautogui.locateCenterOnScreen()               # add new customer

# driver code to populate the address book
for row in range(rowNum):
    currentRow = list(customerDF.loc[row])
    currID = currentRow[ID]
    currCity = currentRow[City]

    #
    print(currentRow)
