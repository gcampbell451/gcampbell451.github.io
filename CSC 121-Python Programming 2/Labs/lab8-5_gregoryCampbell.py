# Gregory Campbell      January 6, 2022         Alphabetic Telephone Number Translator
"""
    This program asks the user to enter a 10-character telephone number
    in the format XXX-XXX-XXXX and coverts any alphabetic characters in
    that string to their digital equivalents based on the letters on 
    a telephone keypad.
"""
#======================== main method
def main():
    # begin loop to keep program running
    keep_going = 'y'
    while keep_going.lower() == 'y':
        # get user string entry
        user_num = input('\nEnter a 10-character phone number in the format XXX-XXX-XXXX, \nusing numbers and/or alphabetic characters (e.g. 555-GET-FOOD): >> ')

        # translate the entry
        translated_num = translate_to_phone(user_num)

        # display output
        print(f'\nThat telphone number is {translated_num}.')

        # ask user to continue or quit
        keep_going = keep_running_program()

    # print goodbye message
    display_goodbye_message()

#====================== helper methods

# display_heading displays a heading for the program instance
def display_heading():
    print('\n String Digit Summation')
    print('========================')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nWould you like to enter another string of characters? (Y/N) ")

# translate_to_phone creates an empty string, translates the characters in 
# the user-supplied string to their telephone keypad equivalent, adds each
# character to the empty string, and returns the filled string
def translate_to_phone(num):
    new_num = ''
    for char in num: 
        if char in '0123456789-':
            new_num += char
        if char.lower() in 'abc':
            new_num += '2'
        if char.lower() in 'def':
            new_num += '3'
        if char.lower() in 'ghi':
            new_num += '4'
        if char.lower() in 'jkl':
            new_num += '5'
        if char.lower() in 'mno':
            new_num += '6'
        if char.lower() in 'pqrs':
            new_num += '7'
        if char.lower() in 'tuv':
            new_num += '8'
        if char.lower() in 'wxyz':
            new_num += '9'

    return new_num

# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


# call main
if __name__ == '__main__':
    main()


