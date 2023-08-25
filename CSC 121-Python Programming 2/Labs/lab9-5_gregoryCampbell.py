# Gregory Campbell      lab9-5        February 10, 2022
"""
    This program reads in a text file and creates a dictionary using
    each word in the file as the key with the values representing how
    many times that word appears in the file. The word and the frequency 
    that each word appears is then displayed.
"""
#======================== main method
import ast  # needed to convert string to dictionary
def main():
    # display heading
    display_heading()

    # begin loop to keep program running
    keep_going = 'y'
    while keep_going.lower() == 'y':
        # create file object to read text file
        infile = open('text95.txt', 'r')

        # process file, converting it to a string with words separated by spaces
        infile_string = process_file(infile)
        
        # close the file
        infile.close()

        # split string into list
        word_list = infile_string.split()

        # create empty dictionary from word_list
        dictionary = create_dictionary(word_list)

        # display the frequency of each word
        display_results(dictionary)

        # ask user to continue or quit
        keep_going = keep_running_program()

    # print goodbye message
    display_goodbye_message()

#======================  methods

# display_heading displays a heading for the program instance
def display_heading():
    print('\n Word Counter')
    print('==============\n')

# process_file converts its contents to a string with words separated by spaces
def process_file(infile):
    # create empty string
    infile_string = ''

    # iterate over lines in file
    for line in infile:
        # change all characters to lower case
        line = line.lower()

        # strip newlines, replace with spaces so string can be split later
        line = line.replace('\n', ' ')
        infile_string += line

        # remove dashes, commas, and periods 
        infile_string = infile_string.replace('-', ' ')
        infile_string = infile_string.replace(',', '')
        infile_string = infile_string.replace('.', '')

    return infile_string

# create_dictionary takes word_list and creates a dictionary of unique words and their counts
def create_dictionary(word_list):
    # create empty dictionary
    dictionary = {}

    # iterate over infile_string, adding words as keys
    for word in word_list:
        # if the word is not in the dictionary, add it, initializing its count to 1
        if word not in dictionary:
            dictionary[word] = 1
        
        # if the word is present in the dictionary, get its current count, increment it, and replace it 
        else:
            count = dictionary.get(word)
            count += 1
            dictionary[word] = count
    
    return dictionary

# display_results displays the words in the dictionary and the number of times they apper in the source file
def display_results(dictionary):
    print(' Word: Count')
    print('-------------')

    # print word and count
    for key, value in dictionary.items():
        print(f'{key}: {value}')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nWould you like run the program again? This will simply redisplay the output. (Y/N)>> ")

# display_goodbye_message confirms program has ended by user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#============================== call main
if __name__ == '__main__':
    main()


