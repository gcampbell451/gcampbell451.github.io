# Gregory Campbell   April 15, 2022     GCampbell_project2.py
"""
This program asks the user to select which data from an external file containing
COVID data from States. The user will select reporting on data by state, date, and
cases and/or deaths. The user will also choose whether to get a line or a bar chart.

"""   


#========== main
def main():
    # display program header
    display_header()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # ask user which data they want to graph
        report_choice = get_report_choice()
        
        # branch based on choice
        if report_choice == 1:
            #  ask user whether they want data by state or month, branch based on choice
            state_or_month = get_state_or_month_choice()
            if state_or_month == 1:
                state_choice = get_state_choice()

                # ask user whether they want to graph cases and/or deaths
                cases_and_or_deaths = get_cases_and_or_deaths()

                # ask user whether they want a bar or line graph, branch based on choice
                bar_or_line = get_bar_or_line()

                #produce graph

            else:
                month_choice = get_month_choice()

                # ask user whether they want to graph cases and/or deaths
                cases_and_or_deaths = get_cases_and_or_deaths()

                # ask user whether they want a bar or line graph, branch based on choice
                bar_or_line = get_bar_or_line()

                #produce graph
            
        elif report_choice == 2:
            # ask user which state they want to graph data for
            state_choice = get_state_choice()

            # ask user which year they want to graph data for
            year_choice = get_year_choice()
            
            # produce graph

        elif report_choice == 3:
            pass
            # produce graph

        else:
            pass
            # produce graph

        # ask user to continue or quit
        keep_going = keep_running_program()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print('\n United States COVID-19 Cases and Deaths by State over Time ')
    print('============================================================')

# get_report_choice gets user's reporting choice and validates input
def get_report_choice():
    report_choice = int(input('\nWhat data do you want to graph?\n\n\t' +
                        '1. Daily Cases and/or Deaths for a single state/month\n\t' +
                        '2. Monthly Cases and/or Deaths for one state for a year\n\t' +
                        '3. Total Cases and/or Deaths for all states by year\n\t' +
                        '4. Monthly Data for multiple years\n\n' +
                        'Enter 1, 2, 3, or 4: '))

    return validate_4(report_choice)

# get_state_or_month_choice gets user's reporting choice and validates input
def get_state_or_month_choice():
    state_or_month_choice = int(input('\nDo you want reporting by state or month?\n\n\t' +
                                    '1. State\n\t' +
                                    '2. Month\n\n' + 
                                    'Enter 1 or 2: '))

    return validate_2(state_or_month_choice)

# get_state_choice gets user's reporting choice and validates input
def get_state_choice():
    # create list of 2-digit state postal codes
    state_list = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 
                  'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or',
                  'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']
    state_choice = input('\nFor which state do you want to graph data? Use two-digit postal code: ')
    
    # validate input
    state_choice = state_choice.lower()
    while state_choice not in state_list:
        print('Invalid input. You must enter a valid two-digit postal code.')
        state_choice = input('\nWhich state do you want to see data for? Use two-digit postal code: ')
        state_choice = state_choice.lower()

    return state_choice

# get_cases_and_or_deaths gets user's reporting choice and validates input
def get_cases_and_or_deaths():
    cases_and_or_deaths = int(input('\n Do you want to graph cases and/or deaths?\n\n\t' +
                               '1. Cases\n\t2. Deaths\n\t3. Cases and Deaths\n\nEnter 1, 2, or 3: '))

    return validate_3(cases_and_or_deaths)

# get_month_choice gets user's reporting choice and validates input
def get_month_choice():
    month_choice = int(input('\nFor which month do you want to graph data?\n\n\t' +
                             ' 1. January\n\t 2. February\n\t 3. March\n\t 4. April\n\t 5. May\n\t 6. June\n\t 7. July\n\t 8. August\n\t' +
                             ' 9. September\n\t10. October\n\t11. November\n\t12. December\n\nEnter a number from 1-12: '))

    return validate_12(month_choice)

# get_bar_or_line gets user's reporting choice and validates input
def get_bar_or_line():
    bar_or_line = int(input('\nWhich type of graph do you want to see?\n\n\t1. Bar\n\t2. Line\n\nEnter 1 or 2: '))

    return validate_2(bar_or_line)

# get_year_choice gets user's reporting choice and validates input
def get_year_choice():
    year_choice = int(input('For which year do you want to graph data?\n\n\t1. 2020\n\t2. 2021\n\t3. 2022\n\nEnter 1, 2, or 3: '))

    return validate_3(year_choice)


# validate_2 ensures the player picks one of the two choices
def validate_2(answer):
    while answer < 1 or answer > 2:
        print('\nInvalid input. Input must be 1 or 2.')
        answer = int(input('\nEnter 1 or 2: '))

    return answer

# validate_3 ensures the player picks one of the three choices
def validate_3(answer):
    while answer < 1 or answer > 3:
        print('\nInvalid input. Input must be 1, 2, or 3.')
        answer = int(input('\nEnter 1, 2, or 3: '))

    return answer

# validate_4 ensures the player picks one of the four choices
def validate_4(answer):
    while answer < 1 or answer > 4:
        print('\nInvalid input. Input must be 1, 2, 3, or 4.')
        answer = int(input('\nEnter 1, 2, 3, or 4: '))

    return answer

# validate_12 ensures the player picks one of the twelve choices
def validate_12(answer):
    while answer < 1 or answer > 12:
        print('\nInvalid input. Input must be between 1-12.')
        answer = int(input('\nEnter a number from 1-12: '))

    return answer

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to plot another graph? (Y/N) ") 

# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========== call main
if __name__ == '__main__':
    main()