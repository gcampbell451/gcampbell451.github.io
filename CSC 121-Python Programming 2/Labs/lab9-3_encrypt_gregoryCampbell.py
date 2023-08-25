# Gregory Campbell      lab9-3 encrypt       January 12, 2022
"""
    This module reads in a dictionary and an unencrypted file and uses
    the dictionary to encrypt the file, writing to an output file.
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

        # read in unencrypted file
        unencrypted_infile = open('unencryptedText.txt', 'r')

        # create file object to write outfile
        outfile = open('encryptedText.txt', 'w')

        # iterate over unencrypted_infile
        for line in unencrypted_infile:
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

            # write  writeStr to outfile
            outfile.write(writeStr)
            
        # close all files
        dictionary_infile.close()
        unencrypted_infile.close()
        outfile.close()
               
        # ask user to continue or quit
        keep_going = keep_running_program()

    # print goodbye message
    display_goodbye_message()

#====================== helper methods

# display_heading displays a heading for the program instance
def display_heading():
    print('\n File Encrypter')
    print('================\n')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nWould you like run the program again? This will overwrite the existing output file. (Y/N)>> ")

# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


# call main
if __name__ == '__main__':
    main()


