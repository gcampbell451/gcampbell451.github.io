# Gregory Campbell      lab 11-1    February 23, 2022
"""
    This program creates an object of the ProductionWorker class and prompts the user to 
    enter data for each of the object's data attributes. The object's accessor methods are
    then used to display this data.
"""
import employee

#========== main
def main():
    # display program header
    display_header()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':
        # get user information
        name, number, shift_number, pay = get_user_info()
        
        # create a ProductionWorker object
        new_employee = employee.ProductionWorker(name, number, shift_number, pay)

        # display employee information
        display_info(new_employee)
        
        # ask user to continue or quit
        keep_going = keep_running_program()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print('\n Enter Employee Information ')
    print('============================')

# get_user_info prompts user for the employee's information, returns it to main
def get_user_info():
    name = input("Employee's Name: ")
    number = input("Employee's Number: ")
    shift_number = validate_shift_number()
    pay = validate_pay()

    return name, number, shift_number, pay

# validate_shift_number ensures the user picks one of the two choices
def validate_shift_number():
    shift_number = int(input("Employee's Shift (1 = Day, 2 = Night): "))
    while shift_number < 1 or shift_number > 2:
        print('Invalid input. Please enter 1 or 2')
        shift_number = int(input("Employee's Shift (1 = Day, 2 = Night): "))

    return shift_number

# validate_pay ensures the user enters a positive number
def validate_pay():
    pay = float(input("Employee's Hourly Pay Rate: "))
    while pay <= 0:
        print('Invalid input. Enter a positive number.')
        pay = float(input("Employee's Hourly Pay Rate: "))

    return pay

# display_info displays the employee's information
def display_info(employee):
    print('\n Employee Information ')
    print('----------------------')
    print(f'Employee Name: {employee.get_employee_name()}')
    print(f'Employee Number: {employee.get_employee_number()}')
    if employee.get_shift_number() == 1:
        print(f'Employee Shift: Day')
    else:
        print(f'Employee Shift: Night')
    print(f'Employee Pay: ${employee.get_hourly_pay_rate():,.2f}/hr')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to enter information for another employee? (Y/N) ") 

# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========== call main
if __name__ == '__main__':
    main()