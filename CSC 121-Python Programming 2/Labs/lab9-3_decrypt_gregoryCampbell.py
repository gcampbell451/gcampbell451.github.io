# Gregory Campbell      lab9-3 decrypt       January 12, 2022
"""
    This module reads in a dictionary and an encrypted file and uses
    the dictionary to decrypt the file, displaying the contents of the file.
"""
#======================== main method
import ast  # needed to convert string to dictionary
def main():
    # display heading
    display_heading()

    # begin loop to keep program running
    keep_going = 'y'
    while keep_going.lower() == 'y':
        # create file object to read encryptionDictionary infile
        dictionary_infile = open('encryptionDictionary.txt', 'r')

        # create empty string
        decryptStr = ''

        # iterate over file, removing whitespace on left, adding modified line to string
        for line in dictionary_infile:
            line = line.lstrip()
            decryptStr += line

        # remove portion of line 1 to create dictionary in string form
        decryptStr = decryptStr.replace('CODE = ', '')

        # convert string to dictionary
        encryptionDictionary = ast.literal_eval(decryptStr) 
       
        # create file object for encrypted infile
        encrypted_infile = open('encryptedText.txt', 'r')

        # iterate over encrypted_infile
        for line in encrypted_infile:
            # create empty string
            writeStr = ''

            # iterate over line
            for char in line:
                # get value from key in encryptionDictionary
                value = encryptionDictionary.get(char)

                # account for spaces, which do not have a translation
                if (value == None):
                    value = ' '

                # cast value to string type
                value = str(value)

                # concat value to writeStr
                writeStr += value

        # display contents 
        print(writeStr)

        # ask user to continue or quit
        keep_going = keep_running_program()

    # print goodbye message
    display_goodbye_message()

#====================== helper methods

# display_heading displays a heading for the program instance
def display_heading():
    print('\n File Decrypter')
    print('================\n')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nWould you like run the program again? This will simply redisplay the output. (Y/N)>> ")

# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#============================== call main
if __name__ == '__main__':
    main()


