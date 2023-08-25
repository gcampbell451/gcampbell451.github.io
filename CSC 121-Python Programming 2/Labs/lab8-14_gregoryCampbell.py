# Gregory Campbell      lab8-14        January 11, 2022
"""
    This program asks the user to choose from preselected operations to
    be performed on data from a supplied file: the average price per year,
    average price per month, highest and lowest prices per year, list of prices
    from lowest to highest, and list of prices from highest to lowest in
    "GasPrices.txt". The program reads in the data and performs the 
    user-selected calculations.
"""
#======================== main method
def main():
    # display heading
    display_heading()

    # begin loop to keep program running
    keep_going = 'y'
    while keep_going.lower() == 'y':
        # display menu
        display_menu()

        # get user menu choice, validate
        user_choice = validate_choice(int(input('\nEnter your selection (1-5): >> ')))

        # perform operation based on user choice, display output
        if user_choice == 1:
            calc_avg_price_per_year()
        if user_choice == 2:
            calc_avg_price_per_month()
        if user_choice == 3:
            highest_and_lowest_prices_per_year()
        if user_choice == 4:
            list_of_prices_lowest_to_highest()
        if user_choice == 5:
            list_of_prices_highest_to_lowest()        

        # ask user to continue or quit
        keep_going = keep_running_program()

    # print goodbye message
    display_goodbye_message()

#====================== helper methods

# display_heading displays a heading for the program instance
def display_heading():
    print('\n Gas Prices 4/5/1993-8/26/2013')
    print('===============================')

# display_menu displays menu of choices for the user
def display_menu():
    print('\nWhich operation would you like to perform on the dataset?')
    print('\n\t1. Average price per year\n\t2. Average price per month\n\t3. Highest and lowest prices per year\n\t4. List of prices, lowest to highest\n\t5. List of prices, highest to lowest')
    
# validate_choice ensures the user picks one of the menu options
def validate_choice(user_choice):
    while user_choice < 1 or user_choice > 5:
        print('\nInvalid input. Please enter a number between 1-5: >> ')
        user_choice = int(input('\nEnter your selection (1-5): >> '))
    return user_choice

# calc_avg_price_per_year calculates the average price for the year, returns one price
def calc_avg_price_per_year():
    # create file object
    infile = open('GasPrices.txt', 'r')

    # initialize accumulators
    total_1993 = 0
    count_1993 = 0
    total_1994 = 0
    count_1994 = 0
    total_1995 = 0
    count_1995 = 0
    total_1996 = 0
    count_1996 = 0
    total_1997 = 0
    count_1997 = 0
    total_1998 = 0
    count_1998 = 0
    total_1999 = 0
    count_1999 = 0
    total_2000 = 0
    count_2000 = 0
    total_2001 = 0
    count_2001 = 0
    total_2002 = 0
    count_2002 = 0
    total_2003 = 0
    count_2003 = 0
    total_2004 = 0
    count_2004 = 0
    total_2005 = 0
    count_2005 = 0
    total_2006 = 0
    count_2006 = 0
    total_2007 = 0
    count_2007 = 0
    total_2008 = 0
    count_2008 = 0
    total_2009 = 0
    count_2009 = 0
    total_2010 = 0
    count_2010 = 0
    total_2011 = 0
    count_2011 = 0
    total_2012 = 0
    count_2012 = 0
    total_2013 = 0
    count_2013 = 0

    # loop through file, accumulating totals and incrementing counts
    for line in infile:
        if line[6:10] == '1993':
            total_1993 += float(line[11:])
            count_1993 += 1
        elif line[6:10] == '1994':
            total_1994 += float(line[11:])
            count_1994 += 1
        elif line[6:10] == '1995':
            total_1995 += float(line[11:])
            count_1995 += 1
        elif line[6:10] == '1996':
            total_1996 += float(line[11:])
            count_1996 += 1
        elif line[6:10] == '1997':
            total_1997 += float(line[11:])
            count_1997 += 1
        elif line[6:10] == '1998':
            total_1998 += float(line[11:])
            count_1998 += 1
        elif line[6:10] == '1999':
            total_1999 += float(line[11:])
            count_1999 += 1
        elif line[6:10] == '2000':
            total_2000 += float(line[11:])
            count_2000 += 1
        elif line[6:10] == '2001':
            total_2001 += float(line[11:])
            count_2001 += 1
        elif line[6:10] == '2002':
            total_2002 += float(line[11:])
            count_2002 += 1
        elif line[6:10] == '2003':
            total_2003 += float(line[11:])
            count_2003 += 1
        elif line[6:10] == '2004':
            total_2004 += float(line[11:])
            count_2004 += 1
        elif line[6:10] == '2005':
            total_2005 += float(line[11:])
            count_2005 += 1
        elif line[6:10] == '2006':
            total_2006 += float(line[11:])
            count_2006 += 1
        elif line[6:10] == '2007':
            total_2007 += float(line[11:])
            count_2007 += 1
        elif line[6:10] == '2008':
            total_2008 += float(line[11:])
            count_2008 += 1
        elif line[6:10] == '2009':
            total_2009 += float(line[11:])
            count_2009 += 1
        elif line[6:10] == '2010':
            total_2010 += float(line[11:])
            count_2010 += 1
        elif line[6:10] == '2011':
            total_2011 += float(line[11:])
            count_2011 += 1
        elif line[6:10] == '2012':
            total_2012 += float(line[11:])
            count_2012 += 1
        elif line[6:10] == '2013':
            total_2013 += float(line[11:])
            count_2013 += 1
        
    # close the file
    infile.close()

    # display results
    print('\n Average Price per Year 1993-2013')
    print('==================================\n')
    print(f'1993: ${(total_1993 / count_1993):.2f}')
    print(f'1994: ${(total_1994 / count_1994):.2f}')
    print(f'1995: ${(total_1995 / count_1995):.2f}')
    print(f'1996: ${(total_1996 / count_1996):.2f}')
    print(f'1997: ${(total_1997 / count_1997):.2f}')
    print(f'1998: ${(total_1998 / count_1998):.2f}')
    print(f'1999: ${(total_1999 / count_1999):.2f}')
    print(f'2000: ${(total_2000 / count_2000):.2f}')
    print(f'2001: ${(total_2001 / count_2001):.2f}')
    print(f'2002: ${(total_2002 / count_2002):.2f}')
    print(f'2003: ${(total_2003 / count_2003):.2f}')
    print(f'2004: ${(total_2004 / count_2004):.2f}')
    print(f'2005: ${(total_2005 / count_2005):.2f}')
    print(f'2006: ${(total_2006 / count_2006):.2f}')
    print(f'2007: ${(total_2007 / count_2007):.2f}')
    print(f'2008: ${(total_2008 / count_2008):.2f}')
    print(f'2009: ${(total_2009 / count_2009):.2f}')
    print(f'2010: ${(total_2010 / count_2010):.2f}')
    print(f'2011: ${(total_2011 / count_2011):.2f}')
    print(f'2012: ${(total_2012 / count_2012):.2f}')
    print(f'2013: ${(total_2013 / count_2013):.2f}')

# calc_avg_price_per_month calculates the average price per month
def calc_avg_price_per_month():
    # initialize accumulators
    total_jan = 0
    count_jan = 0
    total_feb = 0
    count_feb = 0
    total_mar = 0
    count_mar = 0
    total_apr = 0
    count_apr = 0
    total_may = 0
    count_may = 0
    total_jun = 0
    count_jun = 0
    total_jul = 0
    count_jul = 0
    total_aug = 0
    count_aug = 0
    total_sep = 0
    count_sep = 0
    total_oct = 0
    count_oct = 0
    total_nov = 0
    count_nov = 0
    total_dec = 0
    count_dec = 0

    # create file object
    infile = open('GasPrices.txt', 'r')

    # loop through file, accumulating totals and incrementing counts
    for line in infile:
        if line[:2] == '01':
            total_jan += float(line[11:])
            count_jan += 1
        elif line[:2] == '02':
            total_feb += float(line[11:])
            count_feb += 1
        elif line[:2] == '03':
            total_mar += float(line[11:])
            count_mar += 1
        elif line[:2] == '04':
            total_apr += float(line[11:])
            count_apr += 1
        elif line[:2] == '05':
            total_may += float(line[11:])
            count_may += 1
        elif line[:2] == '06':
            total_jun += float(line[11:])
            count_jun += 1
        elif line[:2] == '07':
            total_jul += float(line[11:])
            count_jul += 1
        elif line[:2] == '08':
            total_aug += float(line[11:])
            count_aug += 1
        elif line[:2] == '09':
            total_sep += float(line[11:])
            count_sep += 1
        elif line[:2] == '10':
            total_oct += float(line[11:])
            count_oct += 1
        elif line[:2] == '11':
            total_nov += float(line[11:])
            count_nov += 1
        elif line[:2] == '12':
            total_dec += float(line[11:])
            count_dec += 1

    # close the file
    infile.close()

    # display results
    print('\n Average Price per Month 1993-2013')
    print('===================================\n')
    print(f'January:\t${(total_jan/count_jan):.2f}')
    print(f'February:\t${(total_feb/count_feb):.2f}')
    print(f'March:\t\t${(total_mar/count_mar):.2f}')
    print(f'April:\t\t${(total_apr/count_apr):.2f}')
    print(f'May:\t\t${(total_may/count_may):.2f}')
    print(f'June:\t\t${(total_jun/count_jun):.2f}')
    print(f'July:\t\t${(total_jul/count_jul):.2f}')
    print(f'August:\t\t${(total_aug/count_aug):.2f}')
    print(f'September:\t${(total_sep/count_sep):.2f}')
    print(f'October:\t${(total_oct/count_oct):.2f}')
    print(f'November:\t${(total_nov/count_nov):.2f}')
    print(f'December:\t${(total_dec/count_dec):.2f}')

# highest_and_lowest_prices_per_year reads in an external file, parses 
# each line, keeps track of the highest and lowest prices per year, and
# displays the result
def highest_and_lowest_prices_per_year():
    # initialize accumulators
    high_93 = 0.0       # accumulators are arbitrarily large and small to ensure
    low_93 = 100.0      # the first element selected will be assigned to the variable
    high_94 = 0.0
    low_94 = 100.0
    high_95 = 0.0
    low_95 = 100.0
    high_96 = 0.0
    low_96 = 100.0
    high_97 = 0.0
    low_97 = 100.0
    high_98 = 0.0
    low_98 = 100.0
    high_99 = 0.0
    low_99 = 100.0
    high_00 = 0.0
    low_00 = 100.0
    high_01 = 0.0
    low_01= 100.0
    high_02 = 0.0
    low_02= 100.0
    high_03 = 0.0
    low_03 = 100.0
    high_04 = 0.0
    low_04 = 100.0
    high_05 = 0.0
    low_05 = 100.0
    high_06 = 0.0
    low_06 = 100.0
    high_07 = 0.0
    low_07 = 100.0
    high_08 = 0.0
    low_08 = 100.0
    high_09 = 0.0
    low_09 = 100.0
    high_10 = 0.0
    low_10 = 100.0
    high_11 = 0.0
    low_11 = 100.0
    high_12 = 0.0
    low_12 = 100.0
    high_13 = 0.0
    low_13 = 100.0

    # create file object
    infile = open('GasPrices.txt', 'r')

    # parse file, keeping track of the highest and lowest prices per year
    for line in infile:
        if line[6:10] == '1993':
            if float(line[11:]) > high_93:
                high_93 = float(line[11:])
            if float(line[11:]) < low_93: 
                low_93 = float(line[11:])
        if line[6:10] == '1994':
            if float(line[11:]) > high_94:
                high_94 = float(line[11:])
            if float(line[11:]) < low_94: 
                low_94 = float(line[11:])
        if line[6:10] == '1995':
            if float(line[11:]) > high_95:
                high_95 = float(line[11:])
            if float(line[11:]) < low_95: 
                low_95 = float(line[11:])
        if line[6:10] == '1996':
            if float(line[11:]) > high_96:
                high_96 = float(line[11:])
            if float(line[11:]) < low_96: 
                low_96 = float(line[11:])
        if line[6:10] == '1997':
            if float(line[11:]) > high_97:
                high_97 = float(line[11:])
            if float(line[11:]) < low_97: 
                low_97 = float(line[11:])
        if line[6:10] == '1998':
            if float(line[11:]) > high_98:
                high_98 = float(line[11:])
            if float(line[11:]) < low_98: 
                low_98 = float(line[11:])
        if line[6:10] == '1999':
            if float(line[11:]) > high_99:
                high_99 = float(line[11:])
            if float(line[11:]) < low_99: 
                low_99 = float(line[11:])
        if line[6:10] == '2000':
            if float(line[11:]) > high_00:
                high_00 = float(line[11:])
            if float(line[11:]) < low_00: 
                low_00 = float(line[11:])
        if line[6:10] == '2001':
            if float(line[11:]) > high_01:
                high_01 = float(line[11:])
            if float(line[11:]) < low_01: 
                low_01 = float(line[11:])
        if line[6:10] == '2002':
            if float(line[11:]) > high_02:
                high_02 = float(line[11:])
            if float(line[11:]) < low_02: 
                low_02 = float(line[11:])
        if line[6:10] == '2003':
            if float(line[11:]) > high_03:
                high_03 = float(line[11:])
            if float(line[11:]) < low_03: 
                low_03 = float(line[11:])
        if line[6:10] == '2004':
            if float(line[11:]) > high_04:
                high_04 = float(line[11:])
            if float(line[11:]) < low_04: 
                low_04 = float(line[11:])
        if line[6:10] == '2005':
            if float(line[11:]) > high_05:
                high_05 = float(line[11:])
            if float(line[11:]) < low_05: 
                low_05 = float(line[11:])
        if line[6:10] == '2006':
            if float(line[11:]) > high_06:
                high_06 = float(line[11:])
            if float(line[11:]) < low_06: 
                low_06 = float(line[11:])
        if line[6:10] == '2007':
            if float(line[11:]) > high_07:
                high_07 = float(line[11:])
            if float(line[11:]) < low_07: 
                low_07 = float(line[11:])
        if line[6:10] == '2008':
            if float(line[11:]) > high_08:
                high_08 = float(line[11:])
            if float(line[11:]) < low_08: 
                low_08 = float(line[11:])
        if line[6:10] == '2009':
            if float(line[11:]) > high_09:
                high_09 = float(line[11:])
            if float(line[11:]) < low_09: 
                low_09 = float(line[11:])
        if line[6:10] == '2010':
            if float(line[11:]) > high_10:
                high_10 = float(line[11:])
            if float(line[11:]) < low_10: 
                low_10 = float(line[11:])
        if line[6:10] == '2011':
            if float(line[11:]) > high_11:
                high_11 = float(line[11:])
            if float(line[11:]) < low_11: 
                low_11 = float(line[11:])
        if line[6:10] == '2012':
            if float(line[11:]) > high_12:
                high_12 = float(line[11:])
            if float(line[11:]) < low_12: 
                low_12 = float(line[11:])
        if line[6:10] == '2013':
            if float(line[11:]) > high_13:
                high_13 = float(line[11:])
            if float(line[11:]) < low_13: 
                low_13 = float(line[11:])

    # display results
    print('\n Highest and Lowest Prices per Year 1993-2003')
    print('==============================================\n')
    print('Year\tHigh\tLow')
    print('=====================') 
    print(f'1993\t${high_93:.2f}\t${low_93:.2f}')
    print(f'1994\t${high_94:.2f}\t${low_94:.2f}')
    print(f'1995\t${high_95:.2f}\t${low_95:.2f}')
    print(f'1996\t${high_96:.2f}\t${low_96:.2f}')
    print(f'1997\t${high_97:.2f}\t${low_97:.2f}')
    print(f'1998\t${high_98:.2f}\t${low_98:.2f}')
    print(f'1999\t${high_99:.2f}\t${low_99:.2f}')
    print(f'2000\t${high_00:.2f}\t${low_00:.2f}')
    print(f'2001\t${high_01:.2f}\t${low_01:.2f}')
    print(f'2002\t${high_02:.2f}\t${low_02:.2f}')
    print(f'2003\t${high_03:.2f}\t${low_03:.2f}')
    print(f'2004\t${high_04:.2f}\t${low_04:.2f}')
    print(f'2005\t${high_05:.2f}\t${low_05:.2f}')
    print(f'2006\t${high_06:.2f}\t${low_06:.2f}')
    print(f'2007\t${high_07:.2f}\t${low_07:.2f}')
    print(f'2008\t${high_08:.2f}\t${low_08:.2f}')
    print(f'2009\t${high_09:.2f}\t${low_09:.2f}')
    print(f'2010\t${high_10:.2f}\t${low_10:.2f}')
    print(f'2011\t${high_11:.2f}\t${low_11:.2f}')
    print(f'2012\t${high_12:.2f}\t${low_12:.2f}')
    print(f'2013\t${high_13:.2f}\t${low_13:.2f}')

# list_of_prices_lowest_to_highest reads in an external file into a list
# and sorts the list from lowest to highest
def list_of_prices_lowest_to_highest():
    # create file object
    infile = open('GasPrices.txt', 'r')

    # create empty list
    prices_list = []

    # write lines into list
    for line in infile:
        new_line = line.strip('\n')    # strip newline characters
        prices_list.append(new_line)

    # close the file
    infile.close()

    # sort list
    prices_list.sort(key = year_sorter)

    # display output
    print('\n List of Prices, Lowest to Highest 1993-2003')
    print('=============================================\n')
    print('Date\t\tPrice')
    print('======================\n')
    for element in prices_list:
        print(f'{element[:10]}\t${float(element[11:]):.2f}')

# list_of_prices_highest_to_lowest reads in an external file into a list
# and sorts the list from highest to lowest
def list_of_prices_highest_to_lowest():
    # create file object
    infile = open('GasPrices.txt', 'r')

    # create empty list
    prices_list = []

    # write lines into list
    for line in infile:
        new_line = line.strip('\n')    # strip newline characters
        prices_list.append(new_line)

    # close the file
    infile.close()
    
    # sort list
    prices_list.sort(key=year_sorter)

    # reverse list
    prices_list.reverse()

    # display output
    print('\n List of Prices, Highest to Lowest 1993-2013')
    print('=============================================\n')
    print('Date\t\tPrice')
    print('======================\n')
    for element in prices_list:
        print(f'{element[:10]}\t${float(element[11:]):.2f}')

# year_sorter creates a key to sort strings in a list from the 11th
# index to the end of the line to sort by price
def year_sorter(line):
     return line[11:]  

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nWould you like to choose another option? (Y/N) ")

# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")


# call main
if __name__ == '__main__':
    main()


