# Automated Address Book Population
## Context
The logistics company I currently work for wants to populate an address book on the Canada Post EST 2.0 software using data from
a pre-filled Excel spreadsheet that has been verified. 

However, this is a tedious task to do manually and doing so may result in errors that would result in costly shipping 
delays and lost product. 

Thus I decided it would be best to automate it using python and pyautogui.

## Procedure


## Notes
- Data needs to be restructured in a specific manner, will likely have to clean it manually
- Country field will always be CANADA
- Province/ Territory will vary depending on the data in the .xlsx
    - use a python dictionary for the province codes
    - can't search within the dropdown, you need to manually scroll/find/click on what you want
- Use LocateOnScreen() to find the add and save address buttons
    - need to take screenshots of them and include their paths

### Relevant Fields
- Variable Fields:
    - ID, City, Address, Postal Code, Province, Email
- Constant Fields:
    - Name, Company

    