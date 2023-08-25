# Gregory Campbell      lab 14-1        April 20, 2022
"""
    This program connects to an external database containing city names and their
    populations and allows the user to choose a query to run on the database from a 
    list. It then displays the query results and asks the user to choose another query
    or quit.
"""
import sqlite3

#========== main
def main():
    # display program header
    display_header()

    # sqlite3.connect method returns an object we will need to refer to later, so we store it in a variable
    conn = sqlite3.connect('cities.db')

    # the cursor method also returns an object,which can access and modify the db, so we store it in a variable
    cur = conn.cursor()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # ask user which query they want to run
        query_choice = get_query_choice()
        
        # branch based on choice
        if query_choice == 1:
            sort_on_pop_asc(cur)
        elif query_choice == 2:
            sort_on_pop_desc(cur)
        elif query_choice == 3:
            sort_on_name(cur)
        elif query_choice == 4:
            display_total_pop(cur)
        elif query_choice == 5:
            display_average_pop(cur)
        elif query_choice == 6:
            display_highest_pop(cur)
        else:
            display_lowest_pop(cur)
       
        # ask user to continue or quit
        keep_going = keep_running_program()

    # close the database connection
    conn.close()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print('\n Search the cities.db Database ')
    print('================================')


# get_report_choice gets user's reporting choice and validates input
def get_query_choice():
    query_choice = int(input('\nWhat query do you want to run?\n\n\t' +
                        '1. Display a list of cities sorted by population, in ascending order\n\t' +
                        '2. Display a list of cities sorted by population, in descending order\n\t' +
                        '3. Display a list of cities sorted by name\n\t' +
                        '4. Display the total population of all the cities\n\t' +
                        '5. Display the average population of all the cities\n\t' +
                        '6. Display the city with the highest population\n\t' +
                        '7. Display the city with the lowest population\n\n' +
                        'Enter a number from 1-7: '))

    return validate_7(query_choice)


# validate_7 ensures the player picks one of the seven choices
def validate_7(answer):
    while answer < 1 or answer > 7:
        print('\nInvalid input. Input must be between 1-7.')
        answer = int(input('\nEnter a number from 1-7: '))

    return answer


# sort_on_pop displays a list of cities sorted by population in ascending order
def sort_on_pop_asc(cur):
    # query the database; the default sort is ascending
    cur.execute('SELECT CityName, Population FROM Cities ORDER BY Population')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n List of Cities in the Cities Table, Sorted by Ascending Population')
    print('--------------------------------------------------------------------\n')
    print('City\t\tPopulation')
    print('--------------------------')

    # iterate through results of query
    for row in results:
        # assign elements of tuple to variables to allow for improved display
        city = row[0]
        pop = row[1]

        # cities with shorter names need an extra tab to line up column 2
        if len(city) < 8:
            print(f'{city}\t\t{pop:,.0f}')
        else:
            print(f'{city}\t{pop:,.0f}')


# sort_on_pop_desc displays a list of cities sorted by population in descending order
def sort_on_pop_desc(cur):
    # query the database
    cur.execute('SELECT CityName, Population FROM Cities ORDER BY Population DESC')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n List of Cities in the Cities Table, Sorted by Descending Population')
    print('---------------------------------------------------------------------\n')
    print('City\t\tPopulation')
    print('--------------------------')
    for row in results:
        # assign elements of tuple to variables to allow for improved display
        city = row[0]
        pop = row[1]

        # cities with shorter names need an extra tab to line up column 2
        if len(city) < 8:
            print(f'{city}\t\t{pop:,.0f}')
        else:
            print(f'{city}\t{pop:,.0f}')


# sort_on_name displays a list of cities sorted by name
def sort_on_name(cur):
    # query the database; the default sort is ascending
    cur.execute('SELECT CityName FROM Cities ORDER BY CityName')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n List of Cities in the Cities Table, Sorted by Name')
    print('-----------------------------------------------------')
    print()
    for row in results:
        print(f'{row[0]}')


# display_total_pop displays the total population of all cities in the table
def display_total_pop(cur):
    # query the database
    cur.execute('SELECT SUM(Population) FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n Total Population of Cities in the Cities Table')
    print('------------------------------------------------')

    # convert tuple to list to format for display
    result_list = list(results[0])

    # assign element of list to variable to allow for improved display
    total_pop = result_list[0]
    print(f'\nTotal Population: {total_pop:,.0f}')


# display_average_pop displays the average population of all cities in the table
def display_average_pop(cur):
    # query the database
    cur.execute('SELECT AVG(Population) FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n Average Population of Cities in the Cities Table')
    print('---------------------------------------------------')

    # convert tuple to list to format for display
    result_list = list(results[0])

    # assign element of list to variable to allow for improved display
    avg_pop = result_list[0]
    print(f'\nAverage Population: {avg_pop:,.0f}')

# display_highest_pop displays the city with the highest population
def display_highest_pop(cur):
    # query the database
    cur.execute('SELECT CityName, MAX(Population) FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n City with the Highest Population in the Cities Table')
    print('------------------------------------------------------')

    # convert tuple to list to format for display
    high_city_list = list(results[0])

    # assign elements of list to variables to allow for improved display
    city = high_city_list[0]
    pop = high_city_list[1]
    print('\nCity\t\tPopulation')
    print('--------------------------')
    print(f'{city}\t\t{pop:,.0f}')


# display_lowest_pop displays the city with the highest population
def display_lowest_pop(cur):
    # query the database
    cur.execute('SELECT CityName, MIN(Population) FROM Cities')

    # fetch the results
    results = cur.fetchall()

    # display the results
    print('\n City with the Lowest Population in the Cities Table')
    print('-----------------------------------------------------')

    # convert tuple to list to format for display
    low_city_list = list(results[0])

    # assign elements of list to variables to allow for improved display
    city = low_city_list[0]
    pop = low_city_list[1]
    print('\nCity\t\tPopulation')
    print('--------------------------')
    print(f'{city}\t{pop:,.0f}')


# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to run another query? (Y/N) ") 


# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


#========== call main
if __name__ == '__main__':
    main()
