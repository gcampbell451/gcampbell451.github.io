# Gregory Campbell  lab11-1     February 22, 2022
"""
    The Employee class holds data for employee objects. It has attributes
    for employee name and employee number and the necessary accessors, 
    mutators, and __init__ method.
"""
class Employee():
    # the __init__ method initializes an employee object
    def __init__(self, employee_name, employee_number):
         self.__employee_name = employee_name
         self.__employee_number = employee_number

    # mutator methods
    # each of these assigns values to the attribute fields
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # accessor methods
    # each of these returns the values of the attribute fields
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number


"""
    The ProductionWorker class holds data for productionWorker objects and extends the Employee class. 
    It has attributes for shift number and hourly pay rate and the necessary accessors, 
    mutators, and __init__ method.
"""

class ProductionWorker(Employee):
    # the __init__ method initializes an productionWorker object
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        # call super's initializer
        Employee.__init__(self, employee_name, employee_number)

        # initialize productionWorker attributes
        self.__shift_number = shift_number
        self.__hourly_pay_rate= hourly_pay_rate

    # mutator methods
    # each of these assigns values to the attribute fields
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # accessor methods
    # each of these returns the values of the attribute fields
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate



