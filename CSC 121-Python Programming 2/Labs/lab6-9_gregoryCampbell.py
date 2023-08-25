# Gregory Campbell  lab 6-9     January 10, 2022
"""
This program reads a given file, "numbers.txt", and calculates
the total and average of the numbers in the file. The program handles any IOError
and ValueError exceptions that are raised.

"""
#======================== main() function

def main():
    
    # initialize variable to keep program running until user wants to quit
    keepGoing = "Y"
    
    # begin program loop
    while keepGoing == "Y" or keepGoing == "y":
        
        # use try/except to gracefully handle exceptions
        try:
            # create a file object
            file = open('numbers.txt', 'r')
            
            # initialize variables to accumulate total, track number of lines in file 
            total = 0
            count = 0

            # use loop to read in the contents of "numbers.txt"
            for line in file:
                
                # convert line to float, store in variable
                amount = float(line)
                
                # accumulate total, increment count 
                total += amount
                count += 1                
                                   
            # calculate average
            average = total / count
            
            # display result
            print(f'\nThe total of the numbers in "numbers.txt" is {total:,.0f} and the average is{average: ,.2f}.')          
        
            # ask user to continue or quit
            keepGoing = keepRunningProgram()
        
        # handle IOError exceptions
        except IOError:
            handleIOError()
            break
        
        # handle ValueError exceptions
        except ValueError:
            handleValueError()
            break 
        
    # print goodbye message
    displayGoodbyeMessage()
    

#======================== helper functions

# keepRunningProgram asks user if they want to continue or quit
def keepRunningProgram():
    return input("\nDo you want to run the program again? (Y/N) ") 

# handleIOError prints a message if an error occurs reading a file
def handleIOError():
    print("An error occured reading the file.")

# handleValueError prints a message if data of the wrong type is read
def handleValueError():
    print("ERROR: All data must be numeric.")
    
# displayGoobyeMessage confirms program has ended by user's choice
def displayGoodbyeMessage():
    print("\nThank you for using this program. Goodbye!")


#======================== call main()

if __name__ == '__main__':
    main()