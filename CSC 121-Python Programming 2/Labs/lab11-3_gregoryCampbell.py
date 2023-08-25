# Gregory Campbell      lab 11-3    March 5, 2022
"""
    This program creates an object of the Customer class and prompts the user to 
    enter data for each of the object's data attributes. The object's accessor methods are
    then used to display this data.
"""

"""
    The Person class holds data for person objects. It has attributes
    for name, address, and telephone number and the necessary accessors, 
    mutators, and __init__ method.
"""
class Person():
    # the __init__ method initializes an employee object
    def __init__(self, name, address, phone_number):
         self.__name = name
         self.__address = address
         self.__phone_number = phone_number

    # mutator methods
    # each of these assigns values to the attribute fields
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # accessor methods
    # each of these returns the values of the attribute fields
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number


"""
    The Customer class holds data for customer objects and extends the Person class. 
    It has attributes for customer number and whether the customer wants to be on a 
    mailing list, and the necessary accessors, mutators, and __init__ method.
"""

class Customer(Person):
    # the __init__ method initializes an productionWorker object
    def __init__(self, name, address, phone_number, customer_number, wants_to_be_on_mailing_list):
        # call super's initializer
        Person.__init__(self, name, address, phone_number)

        # initialize productionWorker attributes
        self.__customer_number = customer_number
        self.__wants_to_be_on_mailing_list = wants_to_be_on_mailing_list

    # mutator methods
    # each of these assigns values to the attribute fields
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_wants_to_be_on_mailing_list(self, wants_to_be_on_mailing_list):
        self.__wants_to_be_on_mailing_list = wants_to_be_on_mailing_list

    # accessor methods
    # each of these returns the values of the attribute fields
    def get_customer_number(self):
        return self.__customer_number

    def get_wants_to_be_on_mailing_list(self):
        return self.__wants_to_be_on_mailing_list


#========== main
def main():
    # display program header
    display_header()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # get user information
        name, address, phone_number, customer_number, wants_to_be_on_mailing_list = get_user_info()
        
        # create a ProductionWorker object
        new_customer = Customer(name, address, phone_number, customer_number, wants_to_be_on_mailing_list)

        # display employee information
        display_info(new_customer)
        
        # ask user to continue or quit
        keep_going = keep_running_program()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print('\n Enter Customer Information ')
    print('============================')

# get_user_info prompts user for the employee's information, returns it to main
def get_user_info():
    name = input("Customer's Name: ")
    address = input("Customer's Address: ")
    phone_number = input("Customer's Phone Number: ")
    customer_number = input("Customer's Customer Number: ")
    wants_to_be_on_mailing_list = validate_list_choice()

    return name, address, phone_number, customer_number, wants_to_be_on_mailing_list

# validate_shift_number ensures the user picks one of the two choices
def validate_list_choice():
    wants_to_be_on_mailing_list = int(input("Customer Wants to be on Mailing List? (1 = Yes, 2 = No): "))
    while wants_to_be_on_mailing_list < 1 or wants_to_be_on_mailing_list > 2:
        print('Invalid input. Please enter 1 or 2')
        wants_to_be_on_mailing_list = int(input("Customer Wants to be on Mailing List? (1 = Yes, 2 = No): "))

    return wants_to_be_on_mailing_list

# display_info displays the employee's information
def display_info(customer):
    print('\n Customer Information ')
    print('----------------------')
    print(f'Customer Name: {customer.get_name()}')
    print(f'Customer Address: {customer.get_address()}')
    print(f'Customer Phone Number: {customer.get_phone_number()}')
    print(f'Customer Customer Number: {customer.get_customer_number()}')
    if customer.get_wants_to_be_on_mailing_list() == 1:
        print(f'Customer Wants to be on Mailing List: Yes')
    else:
        print(f'Customer Wants to be on Mailing List: No')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to enter information for another customer? (Y/N) ") 

# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========== call main
if __name__ == '__main__':
    main()