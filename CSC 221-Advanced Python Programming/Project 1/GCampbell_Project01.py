# Gregory Campbell      Postal Barcode Project01    February 6, 2022
"""
    This program calculates an item's postage and creates a mailing label. The user
    is prompted to choose Single Mailing or Multiple Mailings. If they choose Single Mailing,
    they are prompted for addressing information, the type of item they are mailing, and the 
    weight of the item. This data is used to print a mailing label displaying the calculated 
    postage for the package, the name and address of the addressee, and a barcode translated 
    from a string comprised of the zip code of the addressee plus a check digit into a series 
    of characters. If the user chooses Multiple Mailing, this information is read in from an 
    external file, the information is used to calculate postage and create a barcode, and the
    mailing labels are displayed.
"""
#====================== main method =========================================================

import math # needed for math.ceil() method
def main():
    # display heading
    displayHeader()

    # begin loop to keep program running
    keep_going = 1
    while keep_going != 3:
        # display menu
        displayMenu()

        # get user menu choice, validate
        keep_going = validateUserChoice()
        if keep_going == 1:
            # get user information
            name = input('\nEnter name: ')
            address = input('\nEnter street address: ')
            city = input('\nEnter city: ')
            state = input('\nEnter state: ')

            # validate zip
            zip = validateZip()

            # break zip into individual digits, cast as int type
            digit1 = int(zip[0])
            digit2 = int(zip[1])
            digit3 = int(zip[2])
            digit4 = int(zip[3])
            digit5 = int(zip[4])

            # get type of parcel, weight of parcel, validate input
            type = validateType()
            weight = validateWeight()

            # calculate postage
            postage = calcPostage(type, weight)

            # translate zip and check digit into barcode
            barcode = createBarcode(digit1, digit2, digit3, digit4, digit5)

            # display results
            displayMailingLabel(name, address, city, state, zip, postage, barcode)

        if keep_going == 2:
            processDataFile()

    # print goodbye message
    display_goodbye_message()

#==================== helper methods ==========================================================

# displayHeader displays a heading for the program instance
def displayHeader():
    print('\nWelcome to the Mailing Label Printing System')
    
# displayMenu displays the menu for user input
def displayMenu():
    print('\n\n1--Single Mailing\n2--Multiple Mailings\n3--Quit')

# validateUserChoice ensures the user selects one of the available menu options
def validateUserChoice():
    keep_going = int(input('\nEnter your choice: '))
    while keep_going < 1 or keep_going > 3:
        print('Invalid input. Enter 1, 2, or 3.')
        keep_going = int(input('\nEnter your choice: '))
    
    return keep_going

# validateZip ensures user enters a 5-digit zip code so barcode is proper length
def validateZip():
    zip = input('\nEnter zip code: ')
    while (len(zip) != 5):
        print('Invalid input. Enter a 5-digit zip code: ')
        zip = input('\nEnter zip code: ')

    return zip

# validateType ensures the user selects one of the available menu options
def validateType():
    type = int(input('\nEnter 1 for letter, 2 for large envelope, 3 for parcel: '))
    while type < 1 or type > 3:
        print('\nInvalid input. Enter 1, 2, or 3: ')
        type = int(input('\nEnter 1 for letter, 2 for large envelope, 3 for parcel: '))

    return type

# validateWeight ensures positive weight
def validateWeight():
    weight = float(input('\nEnter weight in ounces: '))
    while (weight <= 0):
        print('Invalid input. Enter a weight greater than 0: ')
        weight = float(input('\nEnter weight in ounces: '))

    return weight

# calcPostage accepts the type of postage and weight and returns the postage
def calcPostage(type, weight):
    # initialize global constants for cost
    BASE_COST_LETTERS_1OZ_OR_LESS = 0.49
    BASE_COST_ENVELOPES_1OZ_OR_LESS = 0.98
    BASE_COST_PARCELS_3OZ_OR_LESS = 2.54
    ADDITIONAL_CHARGE_PER_OZ_LETTERS = 0.22
    ADDITIONAL_CHARGE_PER_OZ_ENVELOPES = 0.22
    ADDITIONAL_CHARGE_PER_OZ_PARCELS = 0.20

    # branch calculation based on type; additional cost is added per ounce or part of ounce above base charge
    if (type == 1):
        postage = BASE_COST_LETTERS_1OZ_OR_LESS + ((math.ceil(weight) - 1) * ADDITIONAL_CHARGE_PER_OZ_LETTERS)
    elif (type == 2):
        postage = BASE_COST_ENVELOPES_1OZ_OR_LESS + ((math.ceil(weight) - 1) * ADDITIONAL_CHARGE_PER_OZ_ENVELOPES)
    else:
        postage = BASE_COST_PARCELS_3OZ_OR_LESS + ((math.ceil(weight) - 3) * ADDITIONAL_CHARGE_PER_OZ_PARCELS)

    return postage

# calcCheckDigit accepts individual digits of zip code and calculates and returns the check digit
def calcCheckDigit(digit1, digit2, digit3, digit4, digit5):
    # sum individual digits
    sum = digit1 + digit2 + digit3 + digit4 + digit5

    # find sum modulo 10
    sumMod = sum % 10

    # subtract 10 from sum modulo 10
    checkDigit = 10 - sumMod

    # in the case that sum mod 10 is 0, checkDigit would have two digits, which is not allowed,
    # so the modulus is taken again to ensure a one-digit check digit
    if (checkDigit == 10):
        checkDigit = checkDigit % 10

    return checkDigit

# createBarcode accepts individual digits of zip code, calculates the check digit, and returns the barcode string 
def createBarcode(digit1, digit2, digit3, digit4, digit5):
 

    # calculate the check digit from barcodeList
    checkDigit = calcCheckDigit(digit1, digit2, digit3, digit4, digit5)

    # add check digit to list
    barcodeList = [digit1, digit2, digit3, digit4, digit5, checkDigit]

    # translate digits into barCode, add to empty string
    barcode = ''
    for item in barcodeList:
        if (item == 0):
            translate = '||:::'
            barcode += translate
        elif (item == 1):
            translate = ':::||'
            barcode += translate
        elif (item == 2):
            translate = '::|:|'
            barcode += translate
        elif (item == 3):
            translate = '::||:'
            barcode += translate
        elif (item == 4):
            translate = ':|::|'
            barcode += translate
        elif (item == 5):
            translate = ':|:|:'
            barcode += translate
        elif (item == 6):
            translate = ':||::'
            barcode += translate
        elif (item == 7):
            translate = '|:::|'
            barcode += translate
        elif (item == 8):
            translate = '|::|:'
            barcode += translate
        else:
            translate = '|:|::'
            barcode += translate
        
    # add vertical lines on each end
    barcode = '|' + barcode + '|'

    return barcode

# displayMailingLabel accepts customer information and displays a mailing label
def displayMailingLabel(name, address, city, state, zip, postage, barcode):
    print(f'\n\n**************${postage:,.2f}\n\n{name}\n\n{address}\n\n{city} {state} {zip}\n\n{barcode}\n')
    
# processDataFile reads a text file and displays mailing labels for each record in the file.
def processDataFile():
    # create a file object
    infile = open('postalBarcodeData.txt', 'r')

    # read the first line, a name field, from the file
    name = infile.readline()

    # if a line was read, keep processing
    while name != '':
        # use try/catch to gracefully handle errors
        try:
            # read remaining fields from record
            address = infile.readline()
            city = infile.readline()
            state = infile.readline()
            zip = infile.readline()
            type = infile.readline()
            weight = infile.readline()

            # consume blank line
            infile.readline()
        
            # strip the newlines
            name = name.rstrip('\n')
            address = address.rstrip('\n')
            city = city.rstrip('\n')
            state = state.rstrip('\n')
            zip = zip.rstrip('\n')
            type = type.rstrip('\n')
            weight = weight.rstrip('\n')

            # break zip into individual digits, cast as int type
            digit1 = int(zip[0])
            digit2 = int(zip[1])
            digit3 = int(zip[2])
            digit4 = int(zip[3])
            digit5 = int(zip[4])
        
            # convert type to int, weight to float
            type = int(type)
            weight = float(weight)

            # calculate the postage for the record
            postage = calcPostage(type, weight)

            # create the barcode, which calculates the check digit for the record
            barcode = createBarcode(digit1, digit2, digit3, digit4, digit5)

            # display the mailing label
            displayMailingLabel(name, address, city, state, zip, postage, barcode)

            # read the name field of the next record
            name = infile.readline()

        # handle IOError exceptions
        except IOError:
            print("An error occured reading the file.")
            break
        
        # handle ValueError exceptions
        except ValueError:
            print("ERROR: Data expected to be numeric was of a different type.")
            break 
        
    # close the file
    infile.close()

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return int(input("\nEnter your choice: "))

# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you\n")

# ====================== call main ================================================
if __name__ == '__main__':
    main()