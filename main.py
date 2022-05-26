# import statements and constants
from pandas import read_excel       # for reading in the data
import pyautogui as pg              # for mouse and keyboard control
from fillBox import fillBox         # to fill in textboxes
import sys                          # to exit
from fillDropdown import fillDropdown # to fill in dropdowns

# dictionary to store the provinces
provinces = {"ON" : "Ontario", "AB" : "Alberta", "MB" : "Manitoba", "PE" : "Prince Edward Island", "NL" : "Newfoundland and Labrador", "BC" : "British Columbia",
             "YT" : "Yukon", "NS" : "Nova Scotia", "QC" : "Quebec", "NU" : "Nunavut", "SK" : "Saskatchewan", "NB" : "New Brunswick", "NT" : "Northwest Territories"
}
ID, CITY, ADDRESS, POSTALCODE, PROVINCE, EMAIL = 0,4,5,6,7          # correspond to indices of current row

CUSTOMERNAME    = "COSMETIC MANAGER"            # constant field
COMPANY         = "SDM-SHOPPERS DRUG MART"      # constant field
COUNTRY         = "CANADA"                      # constant field

# Creating the dataframe
try:
    #rawPath = str(input("Please paste the file path to the customer data: "))
    #goodPath = rawPath.replace("\\", "/")              # fixing the path
    customerDF = read_excel("SDMdata.xlsx")             # give filepath to the datasheet
    rowNum = len(customerDF.index)      # getting the number of data entries for iterating
except:
    print("File not found/ doesn't exist/ something is wrong")
    sys.exit()                          # quit the program

# trying to load in the images 
try:
    # getting the Field coordinates
    # Fields that need to be filled in/ are drop downs
    idField         = pg.locateCenterOnScreen("images/idField.png")
    nameField       = pg.locateCenterOnScreen("images/nameField.png")
    companyField    = pg.locateCenterOnScreen("images/companyField.png")
    cityField       = pg.locateCenterOnScreen("images/cityField.png")            
    addressField    = pg.locateCenterOnScreen("images/addressField.png")
    postalField     = pg.locateCenterOnScreen("images/postalField.png")
    canadaField     = pg.locateCenterOnScreen("images/canadaField.png")
    provinceField   = pg.locateCenterOnScreen("images/provinceField.png")
    emailField      = pg.locateCenterOnScreen("images/emailField.png")

    # Buttons that will need to be pressed
    saveBtn         = pg.locateCenterOnScreen("images/saveBtn.png")                     # save customer
    newCustBtn      = pg.locateCenterOnScreen("images/newCustBtn.png")               # add new customer
    bookBtn         = pg.locateCenterOnScreen("images/addressBookBtn.png")

    # N province fields (for filling the dropdown)
    btnNWT  = pg.locateCenterOnScreen("images/")
    btnNS   = pg.locateCenterOnScreen("images/")
    btnNL   = pg.locateCenterOnScreen("images/")
    btnNU   = pg.locateCenterOnScreen("images/")
    btnNB   = pg.locateCenterOnScreen("images/")
except:
    print("ERROR! One or more images not found, please check file path and settings!")
    sys.exit()

# Open EST 2.0 (user will need to open)
# Open the correct address book (user can open)

# driver code to populate the address book
def main():
    for row in range(rowNum):
        currentRow = list(customerDF.loc[row])

        # Hit the add new customer button (IMPLEMENT)

        fillBox(idField, str(currentRow[ID]))
        fillBox(nameField, CUSTOMERNAME)
        fillBox(companyField, COMPANY)
        fillBox(addressField, str(currentRow[ADDRESS]))
        fillBox(cityField, str(currentRow[CITY]))
        fillDropdown(canadaField, COUNTRY)      # filling in Canada
        fillDropdown(provinceField, str(currentRow[PROVINCE]))
        fillBox(postalField, str(currentRow[POSTALCODE]))
        fillBox(emailField, str(currentRow[EMAIL]))

        # save the customer data (IMPLELMENT)
    return

# test script, just load the first entry into the form
def test():
    currentRow = list(customerDF.loc[0])
    fillBox(idField, str(currentRow[ID]))
    fillBox(nameField, CUSTOMERNAME)
    fillBox(companyField, COMPANY)
    fillBox(addressField, str(currentRow[ADDRESS]))
    fillBox(cityField, str(currentRow[CITY]))
    fillDropdown(canadaField, COUNTRY)      # filling in Canada
    fillDropdown(provinceField, str(currentRow[PROVINCE]))
    fillBox(postalField, str(currentRow[POSTALCODE]))
    fillBox(emailField, str(currentRow[EMAIL]))

    return
