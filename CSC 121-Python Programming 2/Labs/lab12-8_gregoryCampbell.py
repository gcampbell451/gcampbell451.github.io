# Gregory Campbell      lab12-8     March 6, 2022
"""
    This program solves Ackermann's function, a recursive algorithm used to test how well a 
    system optimizes its performance of recursion.
"""

#========== main
def main():
    # display program header
    display_header()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        
        # test Ackermann's function with small values for m and n
        print(f'\nAckermann(0, 0) returns {ackermann(0, 0)}.')
        print(f'Ackermann(0, 1) returns {ackermann(0, 1)}.')
        print(f'Ackermann(1, 0) returns {ackermann(1, 0)}.')
        print(f'Ackermann(1, 1) returns {ackermann(1, 1)}.')
        print(f'Ackermann(2, 0) returns {ackermann(2, 0)}.')
        print(f'Ackermann(2, 1) returns {ackermann(2, 1)}.')
        print(f'Ackermann(2, 2) returns {ackermann(2, 2)}.')
        print(f'Ackermann(3, 0) returns {ackermann(3, 0)}.')
        print(f'Ackermann(3, 1) returns {ackermann(3, 1)}.')
        print(f'Ackermann(3, 2) returns {ackermann(3, 2)}.')
        print(f'Ackermann(3, 3) returns {ackermann(3, 3)}.')

        # ask user to continue or quit
        keep_going = keep_running_program()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print("\nAckermann's Function")
    print('=====================')

# ackermann tests how well a system optimizes its performance of recursion
def ackermann(m, n):
    # the logic is given in the assignment
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to run the program again? (Y/N) ") 

# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========== call main
if __name__ == '__main__':
    main()