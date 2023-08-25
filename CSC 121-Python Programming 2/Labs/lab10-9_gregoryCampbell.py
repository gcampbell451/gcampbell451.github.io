# Gregory Campbell      lab 10-9    February 23, 2022
"""
    This program creates a trivia game for two players using the Question class.
    The game starts with player 1, who tries to answer 5 of 10 trivia questions.
    When a question is displayed, 4 answers are presented. Only one is correct, 
    and if the player selects the correct answer, they get a point. Player 2 then 
    goes. After all answers have been selected, the program displays the numer of 
    points for each payer and declares the player with the most points the winner.
    The program has a list containing 10 Question objects, one for each trivia question. 
"""
import question
import random

#========== main
def main():
    # display program header
    display_header()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # create empty list
        question_list = []

        # create 10 question objects
        question1 = question.Question('What is the capital of New York? ', 'Albany', 'New York City', 'Syracuse', 'Buffalo', 1)
        question2 = question.Question('What is the capital of North Carolina? ', 'Charlotte', 'Greensboro', 'Raleigh', 'Wilmington', 3)
        question3 = question.Question('What is the capital of California? ', 'Los Angeles', 'Sacramento', 'San Diego', 'San Francisco', 2)
        question4 = question.Question('What is the capital of Texas? ', 'Dallas', 'Houston', 'San Antonio', 'Austin', 4)
        question5 = question.Question('What is the capital of Idaho? ', 'Twin Falls', 'Idaho City', 'Boise', 'Idaho Falls', 3)
        question6 = question.Question('What is the capital of Vermont? ', 'Burlington', 'Montpelier', 'Killington', 'Stowe', 2)
        question7 = question.Question('What is the capital of Florida? ', 'Orlando', 'Miami', 'Tallahassee', 'Tampa Bay', 3)
        question8 = question.Question('What is the capital of Michigan? ', 'Ann Arbor', 'Detroit', 'Pointe Blank', 'Lansing', 4)
        question9 = question.Question('What is the capital of New Mexico? ', 'Albuquerque', 'Santa Fe', 'Las Cruces', 'Carlsbad', 1)
        question10 = question.Question('What is the capital of Colorado? ', 'Colorado Springs', 'Denver', 'Aspen', 'Boulder', 2)

        # add question objects to list
        question_list.append(question1)
        question_list.append(question2)
        question_list.append(question3)
        question_list.append(question4)
        question_list.append(question5)
        question_list.append(question6)
        question_list.append(question7)
        question_list.append(question8)
        question_list.append(question9)
        question_list.append(question10)

        # initialize players' scores
        player_one_correct = 0
        player_two_correct = 0
        
        # player one's turn
        display_player_header('Player One')
        
        # ask five questions, increment correct answers
        for i in range(5):
            # get random number
            rand_num = get_rand_num(question_list)

            # print question, answer list, get user answer
            answer = print_question(question_list, rand_num, i)

            # accumulate correct answer if correct
            if answer == question_list[rand_num].get_correct_answer():
                player_one_correct += 1

            # remove the question from the list
            question_list.remove(question_list[rand_num])
            
        # player two's turn
        display_player_header('Player Two')

        # ask five questions, increment correct answers
        for i in range(5):
            # get random number
            rand_num = get_rand_num(question_list)

            # print question, answer list, get user answer
            answer = print_question(question_list, rand_num, i)

            # accumulate correct answer if correct
            if answer == question_list[rand_num].get_correct_answer():
                player_two_correct += 1

            # remove the question from the list
            question_list.remove(question_list[rand_num])

        # display the number of points for each player, declare winner
        display_winner(player_one_correct, player_two_correct)

        # ask user to continue or quit
        keep_going = keep_running_program()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print('\n    Trivia Game')

# display_player_header displays the header for each player in the game
def display_player_header(player):
    print(f'__________________\n\n\n{player}:')

# get_rand_num returns a random number in the range of question_list
def get_rand_num(question_list):
    return random.randint(0, len(question_list) - 1)

# print_question prints question and answer list, returns user answer
def print_question(question_list, rand_num, i):
    print(f'\nQuestion {i + 1}:')
    print(question_list[rand_num].__str__())
    answer = validate_answer()
    return answer

# validate_answer ensures the player picks one of the four choices
def validate_answer():
    answer = int(input('Your answer: '))
    while answer < 1 or answer > 4:
        print('Invalid input. Please enter 1, 2, 3, or 4.')
        answer = int(input('Your answer: '))
    return answer

# display_winner displays players' scores and the winner
def display_winner(player_one_correct, player_two_correct):
    print('_____________________\n')
    print(f'\nPlayer One Score: {player_one_correct}\nPlayer Two Score: {player_two_correct}\n')
    if player_one_correct > player_two_correct:
        print('Player One wins!')
    elif player_one_correct < player_two_correct:
        print('Player Two wins!')
    else:
        print('The game ends in a tie.')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to play the game again? (Y/N) ") 

# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========== call main
if __name__ == '__main__':
    main()