# Gregory Campbell      lab 10-2    February 22, 2022
"""
    This program demonstrates the use of the Car class.
    It creates a car object, then calls the accelerate method
    five times, displaying the car's speed, then calls the
    brake method five times, displaying the car's speed.
"""
import car

#========== main
def main():
    # display program header
    display_header()

    # initialize variable to keep program running until user wants to quit
    keep_going = "Y"
    
    # begin program loop
    while keep_going.lower() == 'y':

        # create a car object
        my_car = car.Car(2013, 'Mazda')

        # accelerate 5 times, printing speed
        print('Begin acceleration!\n')
        for i in range(5):
            my_car.accelerate()
            print(f'Current speed: {my_car.get_speed()}')

        # brake 5 times, printing speed
        print('\nBegin braking!\n')
        for i in range(5):
            my_car.brake()
            print(f'Current speed: {my_car.get_speed()}')
        # ask user to continue or quit
        keep_going = keep_running_program()

    display_goodbye_message()

#========== methods

# display_header displays a header for the output
def display_header():
    print('\n    Car Simulator')
    print('=====================\n')

# keep_running_program asks user if they want to continue or quit
def keep_running_program():
    return input("\nDo you want to run the program again? (Y/N) ") 

# display_goodbye_message confirms program has ended by the user's choice
def display_goodbye_message():
    print("\nThank you for using this program. Goodbye!\n")

#========== call main
if __name__ == '__main__':
    main()