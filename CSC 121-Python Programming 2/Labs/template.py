# Gregory Campbell      lab9-3 decrypt       January 12, 2022
"""
This module reads in a dictionary and an unencrypted file and uses
    the dictionary to encrypt the file, writing to an output file
"""
#======================== main method
def main():
    # display heading
    display_heading()

    # begin loop to keep program running
    keep_going = 'y'
    while keep_going.lower() == 'y':
       

               

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


