# Gregory Campbell      lab12-2     March 6, 2022
"""
    This program accepts two arguments, x and y, and uses recursion to find the value of
    x * y. X and y are assumed to be positive integers.
"""

#========== main
def main():
    # display program header
    display_header()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':

        # prompt the user to enter two numbers to be multiplied
        x = validate_input()
        y = validate_input()

        # use recursive function to return the value of num1 * num2
        product = multiply(x, y)

        # display the product
        display_result(x, y, product)

        # ask user to continue or quit
        keep_going = keep_running_program()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print('\n Multiplication by Recursion')
    print('=============================\n')
    print('The first integer you enter will be multiplied by the second you enter.')


# validate_input ensures the user enters positive integers
def validate_input():
    num = int(input('\nEnter a positive integer: '))
    while num < 1:
        print('\nInvalid input! Please enter a positive integer.')
        num = int(input('\nEnter a positive integer: '))
    return num

# multiply uses recursion to find the product of two numbers
def multiply(x, y):
    if x == 1:
        return y
    elif y == 1:
        return x
    else:
        return x + (multiply(x, y - 1))

# display_result displays the result of the multiplication
def display_result(x, y, product):
    print(f'\nThe product of {x} and {y} is {product}.')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to run the program again? (Y/N) ") 

# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========== call main
if __name__ == '__main__':
    main()