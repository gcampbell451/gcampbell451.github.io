# Gregory Campbell      Final Exam       May 9, 2022
"""
    This program connects to an external database containing city names and their
    populations and allows the user to choose a query to run on the database from a 
    list. It then displays the query results and asks the user to choose another query
    or quit.
"""
import sqlite3

#========================================= main
def main():
    # display program header
    display_header()

    # sqlite3.connect method returns an object we will need to refer to later, so we store it in a variable
    conn = sqlite3.connect('cities.db')

    # the cursor method also returns an object, which can access and modify the db, so we store it in a variable
    cur = conn.cursor()

    # initialize variable to keep program running until user wants to quit
    keep_going = 1

    # begin program loop
    while keep_going != 99:
        # display the menu of choices
        display_menu()

        # ask user which query they want to run
        query_choice = get_query_choice()

        # need a short circuit in case user wants to exit
        keep_going = query_choice

        # branch query selection based on choice
        if query_choice == 1:
           sort_on_pop_asc(cur)
        elif query_choice == 2:
           display_pop_density(cur)
        elif query_choice == 3:
           display_total_pop(cur)
        elif query_choice == 4:
           display_average_pop(cur)
        elif query_choice == 5:
           display_highest_pop(cur) 

    # close the database connection
    conn.close()

    display_goodbye_message()


#========================================== methods

# display_header displays a header for the output
def display_header():
    print('\n Search the cities.db Database ')
    print('================================')


# display_menu displays the menu of choices 
def display_menu():
    print('\nWhat query do you want to run?\n\n\t' +
            '1.  Display a list of cities sorted by population, in ascending order\n\t' +
            '2.  Display population density by city\n\t' +
            '3.  Display the total population of all the cities\n\t' +
            '4.  Display the average population of all the cities\n\t' +
            '5.  Display the city with the highest population\n\t' +
            '99. EXIT\n')

# get_query_choice prompts user to choose a query or exit
def get_query_choice():
    query_choice = int(input('Enter a number from 1-5 or 99 to exit: '))
    while query_choice != 99 and (query_choice < 1 or query_choice > 5):
        print('\nInvalid input!')
        query_choice = int(input('\nEnter a number from 1-5 or 99 to exit: '))

    return query_choice

# sort_on_pop_asc queries the database and sorts the cities by ascending population
def sort_on_pop_asc(cur):
    # query the database; the default sort is ascending
    cur.execute('SELECT CityName, Population FROM Cities ORDER BY Population')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n\n List of Cities in the Cities Table, Sorted by Ascending Population')
    print('--------------------------------------------------------------------\n')
    print(' City\t\tPopulation')
    print('---------------------------')

    # iterate through results of query
    for row in results:
        # assign elements of tuple to variables to allow for improved display
        city = row[0]
        pop = row[1]

        # cities with shorter names need an extra tab to line up column 2
        if len(city) < 8:
            print(f'{city}\t\t{pop:>10,.0f}')
        else:
            print(f'{city}\t{pop:>10,.0f}')
    print('---------------------------\n')


# display_pop_density displays the population density of the cities
def display_pop_density(cur):
    # query the database; the default sort is ascending
    cur.execute('SELECT CityName, Population / Area  FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n\n List of Cities and Population Density in the Cities table')
    print('-----------------------------------------------------------\n')
    print(' City\tPop. Density(ppl/square mile)')
    print('--------------------------------------')

    # iterate through results of query
    for row in results:
        # assign elements of tuple to variables to allow for improved display
        city = row[0]
        pop = row[1]
    
        # cities with shorter names need an extra tab to line up column 2
        if len(city) < 8:
            print(f'{city}\t\t{pop:>10,.0f}')
        else:
            print(f'{city}\t{pop:>10,.0f}') 
    print('--------------------------------------\n')


# display_total_pop displays the total population of all cities in the table
def display_total_pop(cur):
    # query the database
    cur.execute('SELECT SUM(Population) FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n\n Total Population of Cities in the Cities Table')
    print('------------------------------------------------')

    # convert tuple to list to format for display
    result_list = list(results[0])

    # assign element of list to variable to allow for improved display
    total_pop = result_list[0]
    print(f'\nTotal Population: {total_pop:,.0f}')
    print('------------------------------------------------\n')


# display_average_pop displays the average population of all cities in the table
def display_average_pop(cur):
    # query the database
    cur.execute('SELECT AVG(Population) FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n\n Average Population of Cities in the Cities Table')
    print('--------------------------------------------------')

    # convert tuple to list to format for display
    result_list = list(results[0])

    # assign element of list to variable to allow for improved display
    avg_pop = result_list[0]
    print(f'\nAverage Population: {avg_pop:,.0f}')
    print('--------------------------------------------------\n')


# display_highest_pop displays the city with the highest population
def display_highest_pop(cur):
    # query the database
    cur.execute('SELECT CityName, MAX(Population) FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n\n City with the Highest Population in the Cities Table')
    print('------------------------------------------------------')

    # convert tuple to list to format for display
    high_city_list = list(results[0])

    # assign elements of list to variables to allow for improved display
    city = high_city_list[0]
    pop = high_city_list[1]
    print('\n City\t\tPopulation')
    print('---------------------------')
    print(f'{city}\t{pop:,.0f}')
    print('------------------------------------------------------\n')


# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


#=================================== call main
if __name__ == '__main__':
    main()