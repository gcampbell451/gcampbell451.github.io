# Gregory Campbell  lab11-3     March 5, 2022
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



