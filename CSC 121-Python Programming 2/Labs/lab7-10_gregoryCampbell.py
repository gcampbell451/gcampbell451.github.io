# Gregory Campbell  lab 7-10     January 10, 2022
"""
This program asks the user to enter the name of a baseball team and, after reading
from a supplied file, "WorldSeriesWinners.txt", displays the number of time that 
team won the World Series from 1903-2020.

"""
#======================== main() function

def main():
    # display heading
    display_heading()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # ask user which team to query results for
        team = input('Enter a team name (name and nickname): >> ')

        # convert to lower case to facilitate matching
        team_lower = team.lower()
        
        # search file for team names
        wins = parse_file(team_lower)

        # display result
        display_results(team, wins)         
    
        # ask user to continue or quit
        keep_going = keep_running_program()
        
       
        
    # print goodbye message
    display_goodbye_message()
    

#======================== helper functions

# display_heading displays a heading for the program instance
def display_heading():
    print('\n World Series Winners')
    print('======================')

# parse_file opens a file for reading, counts the number of time the
# user-supplied team won, returns the count
def parse_file(team):
    # create file object
    infile = open('WorldSeriesWinners.txt', 'r')

    # initialize accumulator, create empty list
    wins = 0
    winners = []

    # read lines of file
    for line in infile:
        # strip newlines
        line = line.strip('\n')

        # accumulate wins
        if line == team:
            wins += 1

        # add winner to list
        winners.append(line)

    # go through list, incrementing count
    for element in winners:
        if team == element.lower():
            wins += 1

    # close the file
    infile.close()
    
    # return the number of wins
    return wins

# display_results takes in the team and number of wins and displays the results of the search
def display_results(team, wins):
    if wins == 0:
        print(f'The {team} have never won the World Series.')
    elif wins == 1:
        print(f'Between 1903-2020, the {team} won the World Series {wins} time.')
    else:
        print(f'Between 1903-2020, the {team} won the World Series {wins} times.')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to run the program again? (Y/N) ") 
  
# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


#======================== call main()

if __name__ == '__main__':
    main()