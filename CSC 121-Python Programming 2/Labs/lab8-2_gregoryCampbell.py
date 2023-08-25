# Gregory Campbell      lab8-14     January 11, 2022
"""
    This program asks the user to enter a series of single-digit numbers with nothing 
    separating them. The program then displays the sum of all the digits.
"""
#====================== main method
def main():
    # display heading
    display_heading()

    # begin loop to keep program running
    keep_going = 'y'
    while keep_going.lower() == 'y':
        # get string
        digits = input('\nEnter a series of digits with no spaces in between: ')

        # create empty list
        digit_list = []

        # iterate over string, converting strings to ints and adding elements to digitList
        for digit in digits:
            digit = int(digit)
            digit_list.append(digit)

        # sum digits in digit_list
        total = 0       # initialize accumulator
        for digit in digit_list:
            total += digit

        # print sum
        print(f'\nThe sum of the digits you entered is {total}.')

        # ask user to continue or quit
        keep_going = keep_running_program()

    # print goodbye message
    display_goodbye_message()

#====================helper methods

# display_heading displays a heading for the program instance
def display_heading():
    print('\n String Digit Summation')
    print('========================')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nWould you like to enter another string of digits? (Y/N) ")

# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

# call main
if __name__ == '__main__':
    main()