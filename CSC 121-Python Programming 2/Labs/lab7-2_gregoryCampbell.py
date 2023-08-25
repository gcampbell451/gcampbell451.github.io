# Gregory Campbell  lab 7-2     January 10, 2022
"""
This program asks the user how many sets of six-digit lottery numbers to create.
The program then generates the user-defined number of sets of lottery numbers. The first
5 numbers are between 1-69 and unique, and the sixth is between 1-69 and need not
be unique.

"""
import random   # needed to generate random numbers

#======================== main() function

def main():
    # display heading
    display_heading()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going == "Y" or keep_going == "y":
        # ask user how many sets of numbers to generate
        num_sets = int(input('\nHow many sets of lottery numbers do you want to create? >> '))
        print()     # print blank line for display purposes

        # begin loop to create user-defined number of sets
        for i in range(num_sets):
            # create empty list
            num_list = []

            # use loop to generate random numbers, adding them to the list. The python ball will be generated separately
            for j in range(5):
                num = random.randint(1, 69)
                
                # ensure uniqueness; the first number generated will be unique and thus skip the validation loop
                while num in num_list: 
                    num = random.randint(1, 69)

                # add unique number to list
                num_list.append(num)
            
            # sort the list
            num_list.sort()

            # generate python ball
            python_ball = random.randint(1, 69)

            # add python ball to list
            num_list.append(python_ball)

            # display result
            print(f'Set {i +1}: {num_list}')          
    
        # ask user to continue or quit
        keep_going = keep_running_program()
        
       
        
    # print goodbye message
    display_goodbye_message()
    

#======================== helper functions

# display_heading displays a heading for the program instance
def display_heading():
    print('\n Lottery Number Generator')
    print('==========================')

# keepRunningProgram asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to run the program again? (Y/N) ") 


    
# displayGoobyeMessage confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


#======================== call main()

if __name__ == '__main__':
    main()