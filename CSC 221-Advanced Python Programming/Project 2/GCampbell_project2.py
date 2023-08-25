# Gregory Campbell   April 15, 2022     GCampbell_project2.py
"""
This program asks the user to select which data to report from an external file containing
COVID data from States. The user will select reporting on data by state, month, and
cases, or deaths. The user will also choose whether to get a line or a bar chart.

"""  
from datetime import datetime as dt
from matplotlib import pyplot as plt, dates as mdates

#====================== Global Constants for menu choices converted to ints
BAR_GRAPH = 1
STATE_GRAPH = 1
CASES_GRAPH = 1


#====================== main
def main():
    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # open file, read in data
        covid_data = open_file()

        # display program header
        display_header()

        # ask user which data they want to graph
        report_choice = get_report_choice()

        # branch based on choice
        if report_choice == 1:

            #  ask user whether they want data by state or month, branch based on choice
            state_or_month = get_state_or_month_choice()

            if state_or_month == STATE_GRAPH:
                state_choice = get_state_choice()

                # ask user whether they want to graph cases and/or deaths
                cases_or_deaths = get_cases_or_deaths()

                # ask user whether they want a bar or line graph
                bar_or_line = get_bar_or_line()

                #produce graph
                graph_by_state(state_choice, cases_or_deaths, bar_or_line, covid_data)

            else:
                # get month and year for reporting
                month_choice = get_month_choice()

                year_choice = get_year_choice()

                # ask user whether they want to graph cases and/or deaths
                cases_or_deaths = get_cases_or_deaths()

                # ask user whether they want a bar or line graph, branch based on choice
                bar_or_line = get_bar_or_line()

                #produce graph
                graph_by_month(month_choice, year_choice, cases_or_deaths, bar_or_line, covid_data)
                
            
        elif report_choice == 2:
            # ask user which state they want to graph data for
            state_choice = get_state_choice()

            # ask user which year they want to graph data for
            year_choice = get_year_choice()

            # ask user whether they want to graph cases and/or deaths
            cases_or_deaths = get_cases_or_deaths()

            # ask user whether they want a bar or line graph, branch based on choice
            bar_or_line = get_bar_or_line()
            
            # produce graph
            graph_one_state_one_year(state_choice, year_choice, cases_or_deaths, bar_or_line, covid_data)

        elif report_choice == 3:
            # ask user which year they want to graph data for
            year_choice = get_year_choice()

            # ask user whether they want to graph cases and/or deaths
            cases_or_deaths = get_cases_or_deaths()

            # ask user whether they want a bar or line graph, branch based on choice
            bar_or_line = get_bar_or_line()

            # produce graph
            graph_all_states_one_year(year_choice, cases_or_deaths, bar_or_line, covid_data)

        else:
            # ask user which state and years to graph data for
            state_choice = get_state_choice()

            start_year, end_year = get_years_to_graph()

            # ask user whether they want to graph cases and/or deaths
            cases_or_deaths = get_cases_or_deaths()

            # ask user whether they want a bar or line graph, branch based on choice
            bar_or_line = get_bar_or_line()

            # produce graph
            graph_monthly_data(state_choice, start_year, end_year, cases_or_deaths, bar_or_line, covid_data)

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
                        '1. Daily Cases or Deaths for a single state/month\n\t' +
                        '2. Monthly Cases or Deaths for one state for a year\n\t' +
                        '3. Total Cases or Deaths for all states by year\n\t' +
                        '4. Monthly Data for multiple years\n\n' +
                        'Enter 1, 2, 3, or 4: '))

    return validate_4(report_choice)


# get_state_or_month_choice gets user's reporting choice and validates input
def get_state_or_month_choice():
    print('\n                    Reporting Options ')
    print('============================================================')
  
    return validate_2(int(input('\nDo you want reporting by state or month?\n\n\t' +
                                    '1. State\n\t' +
                                    '2. Month\n\n' + 
                                    'Enter 1 or 2: ')))


# get_state_choice gets user's reporting choice and validates input
def get_state_choice():
    print('\n                     Choose a State ')
    print('============================================================')

    # create list of 2-digit state postal codes
    state_list = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 
                  'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR',
                  'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    state_choice = input('\nFor which state do you want to graph data?\n\nUse two-digit postal code: ')
    
    # validate input
    state_choice = state_choice.upper()
    while state_choice not in state_list:
        print('\nInvalid input. You must enter a valid two-digit postal code.')
        state_choice = input('\nFor which state do you want to see data?\n\nUse two-digit postal code: ')
        state_choice = state_choice.upper()

    return state_choice


# get_cases_and_or_deaths gets user's reporting choice and validates input
def get_cases_or_deaths():
    print('\n                   Choose Data to Study ')
    print('============================================================')

    return validate_2(int(input('\n Do you want to graph cases or deaths?\n\n\t' +
                               '1. Cases\n\t2. Deaths\n\nEnter 1 or 2: ')))


# get_month_choice gets user's reporting choice and validates input
def get_month_choice():
    print('\n                     Choose a Month ')
    print('============================================================')

    return validate_12(int(input('\nFor which month do you want to graph data?\n\n\t' +
                             ' 1. January\n\t 2. February\n\t 3. March\n\t 4. April\n\t 5. May\n\t 6. June\n\t 7. July\n\t 8. August\n\t' +
                             ' 9. September\n\t10. October\n\t11. November\n\t12. December\n\nEnter a number from 1-12: ')))


# get_bar_or_line gets user's reporting choice and validates input
def get_bar_or_line():
    print('\n                  Choose Type of Graph ')
    print('============================================================')

    return validate_2(int(input('\nWhich type of graph do you want to see?\n\n\t1. Bar\n\t2. Line\n\nEnter 1 or 2: ')))


# get_year_choice gets user's reporting choice and validates input
def get_year_choice():
    print('\n                     Choose a Year')
    print('============================================================')

    return validate_3(int(input('For which year do you want to graph data?\n\n\t1. 2020\n\t2. 2021\n\t3. 2022\n\nEnter 1, 2, or 3: ')))


# get_years_to_graph gets user's choice for start and end year to graph
def get_years_to_graph():
    print('\n           Choose Start and End Year for Reporting')
    print('============================================================')
    start_year = validate_3(int(input('\nEnter the start year for data\n\n\t1. 2020\n\t2. 2021\n\t3. 2022\n\nEnter 1, 2, or 3: ')))
    end_year = validate_3(int(input('\nEnter the end year for data\n\n\t1. 2020\n\t2. 2021\n\t3. 2022\n\nEnter 1, 2, or 3: ')))
    while end_year < start_year:
        print('Invalid input. The ending year cannot be before the starting year.')
        end_year = validate_3(int(input('\nEnter the end year for data\n\n\t1. 2020\n\t2. 2021\n\t3. 2022\n\nEnter 1, 2, or 3: ')))
        
    return start_year, end_year


# validate_2 ensures the user picks one of the two choices
def validate_2(answer):
    while answer < 1 or answer > 2:
        print('\nInvalid input. Input must be 1 or 2.') 
        answer = int(input('\nEnter 1 or 2: '))

    return answer


# validate_3 ensures the user picks one of the three choices
def validate_3(answer):
    while answer < 1 or answer > 3:
        print('\nInvalid input. Input must be 1, 2, or 3.') 
        answer = int(input('\nEnter 1, 2, or 3: '))

    return answer 


# validate_4 ensures the user picks one of the four choices
def validate_4(answer):
    while answer < 1 or answer > 4:
        print('\nInvalid input. Input must be 1, 2, 3, or 4.')
        answer = int(input('\nEnter 1, 2, 3, or 4: '))

    return answer


# validate_12 ensures the user picks one of the twelve choices
def validate_12(answer):
    while answer < 1 or answer > 12:
        print('\nInvalid input. Input must be between 1-12.')
        answer = int(input('\nEnter a number from 1-12: '))

    return answer


# open_file opens the data file for reading
def open_file():
    infile = open('United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv', 'r')

    # start reading at line 2 to remove column headers
    lines = infile.readlines()[1:]

    # close the file
    infile.close()

    return lines


# graph_by_state passes user's choices for reporting and the data array in for graphing
def graph_by_state(state, cases_or_deaths, bar_or_line, lines):
    # create empty list for x coords, cases, deaths
    dates = []
    cases = []
    deaths = []

    # parse the file for desired information, sort
    date_sortable_list = create_date_sortable_list(lines)

    # iterate over sorted list, conditionally adding elements to the dates, cases, and deaths lists
    for line in date_sortable_list:
        # populate lists based on user choice of state
        if line[1] == state:
            convert_to_int_and_append(line, dates, cases, deaths)

    # branch y-axis output based upon user choice of cases or deaths
    y_coords, y_label, title_type = label_y_axis(cases_or_deaths, cases, deaths)

    # format dates for plotting
    x_coords = dates
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)

    # customize axes
    plt.xticks(x_coords, x_coords, rotation = 'vertical')
    plt.title(f'COVID-19 {title_type} in {state}, 2020-2022')
    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.locator_params(axis = 'x', nbins = 20)

    # display graph
    display_graph(bar_or_line, x_coords, y_coords)
    

def graph_by_month(month, year, cases_or_deaths, bar_or_line, lines):
    # create empty list for x coords, cases, deaths
    dates = []
    cases = []
    deaths = []

    # translate int year choices to int years to compare to datetime object element
    if year == 1:
        year = 2020
    elif year == 2:
        year = 2021
    else:
        year = 2022

    # parse the file for desired information, sort
    date_sortable_list = create_date_sortable_list(lines)

    # tokenize each line in file, removing unnecessary columns
    for line in date_sortable_list:
         # populate lists based on user choice of month, year   
        if line[0].month == month and line[0].year == year:
            convert_to_int_and_append(line, dates, cases, deaths)

    # branch y-axis output based upon user choice of cases or deaths
    y_coords, y_label, title_type = label_y_axis(cases_or_deaths, cases, deaths)

    # format dates for plotting
    x_coords = dates
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)

    # customize axes
    plt.xticks(x_coords, x_coords, rotation = 'vertical')
    plt.title(f'COVID-19 {title_type} in {month}/{year}')
    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.locator_params(axis = 'x', nbins = 20)

    # display graph
    display_graph(bar_or_line, x_coords, y_coords)
    

# graph_one_state_one_year(state_choice, year_choice, cases_or_deaths, bar_or_line, covid_data)
def graph_one_state_one_year(state, year, cases_or_deaths, bar_or_line, lines):
    # create empty list for x coords, cases, deaths
    dates = []
    cases = []
    deaths = []

    # translate int year choices to int years to compare to datetime object element
    if year == 1:
        year = 2020
    elif year == 2:
        year = 2021
    else:
        year = 2022

    # parse the file for desired information, sort
    date_sortable_list = create_date_sortable_list(lines)

    for line in date_sortable_list:
        if line[1] == state and line[0].year == year:
            convert_to_int_and_append(line, dates, cases, deaths)
    
    # branch y-axis output based upon user choice of cases or deaths
    y_coords, y_label, title_type = label_y_axis(cases_or_deaths, cases, deaths)

    # format dates for plotting
    x_coords = dates
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)

    # customize axes
    plt.xticks(x_coords, x_coords, rotation = 'vertical')
    plt.title(f'COVID-19 {title_type} in {state}, {year}')
    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.locator_params(axis = 'x', nbins = 20)

    # display graph
    display_graph(bar_or_line, x_coords, y_coords)


# graph_all_states_one_year 
def graph_all_states_one_year(year, cases_or_deaths, bar_or_line, lines):
    # create empty list for x coords, cases, deaths
    dates = []
    cases = []
    deaths = []

    # translate int year choices to int years to compare to datetime object element
    if year == 1:
        year = 2020
    elif year == 2:
        year = 2021
    else:
        year = 2022

    # parse the file for desired information, sort
    date_sortable_list = create_date_sortable_list(lines)

    # initialize accumulators
    total_cases = 0
    total_deaths = 0
    for line in date_sortable_list:
    
        if line[0].year == year:
            line[2] = int(line[2])
            line[3] = int(line[3])
            total_cases += line[2]
            total_deaths += line[3]
            dates.append(line[0])
            cases.append(total_cases)
            deaths.append(total_deaths)

    # branch y-axis output based upon user choice of cases or deaths
    y_coords, y_label, title_type = label_y_axis(cases_or_deaths, cases, deaths)

    # format dates for plotting
    x_coords = dates
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)

    # customize axes
    plt.xticks(x_coords, x_coords, rotation = 'vertical')
    plt.title(f'COVID-19 {title_type}, USA, {year}')
    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.locator_params(axis = 'x', nbins = 20)

    # display graph
    display_graph(bar_or_line, x_coords, y_coords)


def graph_monthly_data(state, start_year, end_year, cases_or_deaths, bar_or_line, lines):
    # create empty list for x coords, cases, deaths
    dates = []
    cases = []
    deaths = []

    # translate int year choices to int years to compare to datetime object element
    if start_year == 1:
        start_year = 2020
    elif start_year == 2:
        start_year = 2021
    else:
        start_year = 2022

    if end_year == 1:
        end_year = 2020
    elif end_year == 2:
        end_year = 2021
    else:
        end_year = 2022

    # parse the file for desired information, sort
    date_sortable_list = create_date_sortable_list(lines)

    # sorry for the brute force solution, using pandas likely would have been easier but I didn't know if it was allowed
    # initialize bins for each month of each year
    jan2020_cases = 0
    feb2020_cases = 0
    mar2020_cases = 0
    apr2020_cases = 0
    may2020_cases = 0
    jun2020_cases = 0
    jul2020_cases = 0
    aug2020_cases = 0
    sep2020_cases = 0
    oct2020_cases = 0
    nov2020_cases = 0
    dec2020_cases = 0
    jan2021_cases = 0
    feb2021_cases = 0
    mar2021_cases = 0
    apr2021_cases = 0
    may2021_cases = 0
    jun2021_cases = 0
    jul2021_cases = 0
    aug2021_cases = 0
    sep2021_cases = 0
    oct2021_cases = 0
    nov2021_cases = 0
    dec2021_cases = 0
    jan2022_cases = 0
    feb2022_cases = 0
    mar2022_cases = 0
    apr2022_cases = 0
    may2022_cases = 0

    jan2020_deaths = 0
    feb2020_deaths = 0
    mar2020_deaths = 0
    apr2020_deaths = 0
    may2020_deaths = 0
    jun2020_deaths = 0
    jul2020_deaths = 0
    aug2020_deaths = 0
    sep2020_deaths = 0
    oct2020_deaths = 0
    nov2020_deaths = 0
    dec2020_deaths = 0
    jan2021_deaths = 0
    feb2021_deaths = 0
    mar2021_deaths = 0
    apr2021_deaths = 0
    may2021_deaths = 0
    jun2021_deaths = 0
    jul2021_deaths = 0
    aug2021_deaths = 0
    sep2021_deaths = 0
    oct2021_deaths = 0
    nov2021_deaths = 0
    dec2021_deaths = 0
    jan2022_deaths = 0
    feb2022_deaths = 0
    mar2022_deaths = 0
    apr2022_deaths = 0
    may2022_deaths = 0
    
    # fill the bins
    for line in date_sortable_list:
        if line[1] == state:
            line[2] = int(line[2])
            line[3] = int(line[3])
            if line[0].month == 1 and line[0].year == 2020:
                jan2020_cases += line[2]
                jan2020_deaths += line[3]
            elif line[0].month == 1 and line[0].year == 2021:
                jan2021_cases += line[2]
                jan2021_deaths += line[3]
            elif line[0].month == 1 and line[0].year == 2022:
                jan2022_cases += line[2]
                jan2022_deaths += line[3]
            elif line[0].month == 2 and line[0].year == 2020:
                feb2020_cases += line[2]
                feb2020_deaths += line[3]
            elif line[0].month == 2 and line[0].year == 2021:
                feb2021_cases += line[2]
                feb2021_deaths += line[3]
            elif line[0].month == 2 and line[0].year == 2022:
                feb2022_cases += line[2]
                feb2022_deaths += line[3]
            elif line[0].month == 3 and line[0].year == 2020:
                mar2020_cases += line[2]
                mar2020_deaths += line[3]
            elif line[0].month == 3 and line[0].year == 2021:
                mar2021_cases += line[2]
                mar2021_deaths += line[3]
            elif line[0].month == 3 and line[0].year == 2022:
                mar2022_cases += line[2]
                mar2022_deaths += line[3]
            elif line[0].month == 4 and line[0].year == 2020:
                apr2020_cases += line[2]
                apr2020_deaths += line[3]
            elif line[0].month == 4 and line[0].year == 2021:
                apr2021_cases += line[2]
                apr2021_deaths += line[3]
            elif line[0].month == 4 and line[0].year == 2022:
                apr2022_cases += line[2]
                apr2022_deaths += line[3]
            elif line[0].month == 5 and line[0].year == 2020:
                may2020_cases += line[2]
                may2020_deaths += line[3]
            elif line[0].month == 5 and line[0].year == 2021:
                may2021_cases += line[2]
                may2021_deaths += line[3]
            elif line[0].month == 6 and line[0].year == 2020:
                jun2020_cases += line[2]
                jun2020_deaths += line[3]
            elif line[0].month == 6 and line[0].year == 2021:
                jun2021_cases += line[2]
                jun2021_deaths += line[3]
            elif line[0].month == 7 and line[0].year == 2020:
                jul2020_cases += line[2]
                jul2020_deaths += line[3]
            elif line[0].month == 7 and line[0].year == 2021:
                jul2021_cases += line[2]
                jul2021_deaths += line[3]
            elif line[0].month == 8 and line[0].year == 2020:
                aug2020_cases += line[2]
                aug2020_deaths += line[3]
            elif line[0].month == 8 and line[0].year == 2021:
                aug2021_cases += line[2]
                aug2021_deaths += line[3]
            elif line[0].month == 9 and line[0].year == 2020:
                aug2020_cases += line[2]
                aug2020_deaths += line[3]
            elif line[0].month == 9 and line[0].year == 2021:
                aug2021_cases += line[2]
                aug2021_deaths += line[3]
            elif line[0].month == 10 and line[0].year == 2020:
                sep2020_cases += line[2]
                sep2020_deaths += line[3]
            elif line[0].month == 10 and line[0].year == 2021:
                sep2021_cases += line[2]
                sep2021_deaths += line[3]
            elif line[0].month == 11 and line[0].year == 2020:
                oct2020_cases += line[2]
                oct2020_deaths += line[3]
            elif line[0].month == 11 and line[0].year == 2021:
                nov2021_cases += line[2]
                nov2021_deaths += line[3]
            elif line[0].month == 12 and line[0].year == 2020:
                dec2020_cases += line[2]
                dec2020_deaths += line[3]
            else:
                dec2021_cases += line[2]
                dec2021_deaths += line[3]
            
    # build lists to graph data
    if start_year == 2020 and end_year == 2020:
        # using ints for the months facilitates filtering, x_ticks will improve readability of graph
        dates = [1,2,3,4,5,6,7,8,9,10,11,12]
        x_ticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        cases = [jan2020_cases, feb2020_cases, mar2020_cases, apr2020_cases, may2020_cases, jun2020_cases, +
                 jul2020_cases, aug2020_cases, sep2020_cases, oct2020_cases, nov2020_cases, dec2020_cases]
        deaths = [jan2020_deaths, feb2020_deaths, mar2020_deaths, apr2020_deaths, may2020_deaths, jun2020_deaths, +
                  jul2020_deaths, aug2020_deaths, sep2020_deaths, oct2020_deaths, nov2020_deaths, dec2020_deaths]
    elif start_year == 2020 and end_year == 2021:
        dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        x_ticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        cases = [jan2020_cases, feb2020_cases, mar2020_cases, apr2020_cases, may2020_cases, jun2020_cases, +
                 jul2020_cases, aug2020_cases, sep2020_cases, oct2020_cases, nov2020_cases, dec2020_cases, +
                 jan2021_cases, feb2021_cases, mar2021_cases, apr2021_cases, may2021_cases, jun2021_cases, +
                 jul2021_cases, aug2021_cases, sep2021_cases, oct2021_cases, nov2021_cases, dec2021_cases]
        deaths = [jan2020_deaths, feb2020_deaths, mar2020_deaths, apr2020_deaths, may2020_deaths, jun2020_deaths, +
                  jul2020_deaths, aug2020_deaths, sep2020_deaths, oct2020_deaths, nov2020_deaths, dec2020_deaths, +
                  jul2021_deaths, aug2021_deaths, sep2021_deaths, oct2021_deaths, nov2021_deaths, dec2021_deaths]
    elif start_year == 2020 and end_year == 2022:
        dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        x_ticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr']
        cases = [jan2020_cases, feb2020_cases, mar2020_cases, apr2020_cases, may2020_cases, jun2020_cases, +
                 jul2020_cases, aug2020_cases, sep2020_cases, oct2020_cases, nov2020_cases, dec2020_cases, +
                 jan2021_cases, feb2021_cases, mar2021_cases, apr2021_cases, may2021_cases, jun2021_cases, +
                 jul2021_cases, aug2021_cases, sep2021_cases, oct2021_cases, nov2021_cases, dec2021_cases, +
                 jan2022_cases, feb2022_cases, mar2022_cases, apr2022_cases]
        deaths = [jan2020_deaths, feb2020_deaths, mar2020_deaths, apr2020_deaths, may2020_deaths, jun2020_deaths, +
                  jul2020_deaths, aug2020_deaths, sep2020_deaths, oct2020_deaths, nov2020_deaths, dec2020_deaths, +
                  jul2021_deaths, aug2021_deaths, sep2021_deaths, oct2021_deaths, nov2021_deaths, dec2021_deaths, +
                  jan2022_deaths, feb2022_deaths, mar2022_deaths, apr2022_deaths]
    elif start_year == 2021 and end_year == 2021:
        dates = [1,2,3,4,5,6,7,8,9,10,11,12]
        x_ticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        cases = [jan2021_cases, feb2021_cases, mar2021_cases, apr2021_cases, may2021_cases, jun2021_cases, +
                 jul2021_cases, aug2021_cases, sep2021_cases, oct2021_cases, nov2021_cases, dec2021_cases]
        deaths = [jan2021_deaths, feb2021_deaths, mar2021_deaths, apr2021_deaths, may2021_deaths, jun2021_deaths, +
                  jul2021_deaths, aug2021_deaths, sep2021_deaths, oct2021_deaths, nov2021_deaths, dec2021_deaths]
    elif start_year == 2021 and end_year == 2022:
        dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        x_ticks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr']
        cases = [jan2021_cases, feb2021_cases, mar2021_cases, apr2021_cases, may2021_cases, jun2021_cases, +
                 jul2021_cases, aug2021_cases, sep2021_cases, oct2021_cases, nov2021_cases, dec2021_cases, +
                 jan2022_cases, feb2022_cases, mar2022_cases, apr2022_cases]
        deaths = [jan2021_deaths, feb2021_deaths, mar2021_deaths, apr2021_deaths, may2021_deaths, jun2021_deaths, +
                  jul2021_deaths, aug2021_deaths, sep2021_deaths, oct2021_deaths, nov2021_deaths, dec2021_deaths, +
                  jan2022_deaths, feb2022_deaths, mar2022_deaths, apr2022_deaths]
    else:
        dates = [1,2,3,4]
        x_ticks = ['Jan', 'Feb', 'Mar', 'Apr']
        cases = [jan2022_cases, feb2022_cases, mar2022_cases, apr2022_cases]
        deaths = [jan2022_deaths, feb2022_deaths, mar2022_deaths, apr2022_deaths]

    # branch y-axis output based upon user choice of cases or deaths
    y_coords, y_label, title_type = label_y_axis(cases_or_deaths, cases, deaths)

    # format dates for plotting
    x_coords = dates
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)

    # customize axes
    plt.xticks(x_coords, x_ticks, rotation = 'vertical')
    plt.title(f'COVID-19 {title_type}, {state}, {start_year}-{end_year}')
    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.locator_params(axis = 'x', nbins = 20)

    # display graph
    display_graph(bar_or_line, x_coords, y_coords)


# create_date_sortable_list removes unwanted data, manipulates date strings for formatting, converts string to date
# object, sorts list 
def create_date_sortable_list(lines):
    # create empty list
    date_sortable_list = []

    # tokenize each line in file, removing unnecessary columns
    for line in lines:
        tokens = line.split(',')
        tokens = tokens[:8]
        del tokens[3:7]
        
        # add leading zero if month is single digit
        day = tokens[0]
        if day[1] == '/':
            day = '0' + day

        # insert a leading zero if day is single digit
        if day[4] == '/':
            day = day[:3] + '0' + day[-6:]

        # convert date string to date object
        format_str = '%m/%d/%Y'
        date_obj = dt.strptime(day, format_str)

        # remove time from date_obj
        date_obj = date_obj.date()
        
        # create new list to append lists to a sortable list
        new_list = [date_obj, tokens[1], tokens[2], tokens[3]]

        # add tokens to new list
        date_sortable_list.append(new_list)

    # sort the new list(since the date object is the first item, default sorting will do)
    date_sortable_list.sort()

    return date_sortable_list


# convert_to_int_and_append converts the strings in the list to ints, appends values to the proper list
def convert_to_int_and_append(line, dates, cases, deaths):
    line[2] = int(line[2])
    line[3] = int(line[3])
    dates.append(line[0])
    cases.append(line[2])
    deaths.append(line[3])


#  display_graph displays the user's choice of graph
def display_graph(bar_or_line, x_coords, y_coords):
    if bar_or_line == BAR_GRAPH:
        plt.bar(x_coords, y_coords)
        plt.show()
    else: 
        plt.plot(x_coords, y_coords)
        plt.show()


# label_y_axis assigns the list to use and the label for the y-axis    
def label_y_axis(cases_or_deaths, cases, deaths):
    if cases_or_deaths == CASES_GRAPH:
        y_coords = cases
        y_label = 'Cases'
        title_type = 'Cases'
    else:
        y_coords = deaths
        y_label = 'Deaths'
        title_type = 'Deaths'

    return y_coords, y_label, title_type


# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to plot another graph? (Y/N) ") 


# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


#========== call main
if __name__ == '__main__':
    main()