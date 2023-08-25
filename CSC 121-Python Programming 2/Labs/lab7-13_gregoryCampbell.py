# Gregory Campbell  lab 7-13     January 11, 2022
"""
This program simulates a Magic 8 Ball. The user is prompted to input a 
yes or no question. The program reads in responses from an external file,
"8_ball_responses.txt", generates a random number, and uses that random
number to select that item from the list and displays the answer. 
"""
#======================== main() function
import random   # needed to generate random numbers
def main():
    # display heading
    display_heading()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # ask user which team to query results for
        query = input('\nAsk the Magic 8 Ball a yes/no question: >> ')

        # display result
        display_results(query)         
    
        # ask user to continue or quit
        keep_going = keep_running_program()
        
    # print goodbye message
    display_goodbye_message()
    
#======================== helper functions

# display_heading displays a heading for the program instance
def display_heading():
    print('\n Magic 8 Ball Simulator')
    print('========================')

# display_results takes in the team and number of wins and displays the results of the search
def display_results(query):
    # create file object
    infile = open('8_ball_responses.txt', 'r')

    # create empty list, read file contents into list
    response_list = []
    for line in infile:
        # strip newline character
        new_line = line.strip('\n')
        response_list.append(new_line)

    # close file
    infile.close()

    # generate random number 
    rand_index = random.randint(0, len(response_list))

    # print the response at rand_index
    print(f'\nYou asked the Magic 8 Ball "{query}".\n\nIts response: {response_list[rand_index]}')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nWould you like to ask the Magic 8 Ball another question? (Y/N) ") 
  
# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#======================== call main()

if __name__ == '__main__':
    main()