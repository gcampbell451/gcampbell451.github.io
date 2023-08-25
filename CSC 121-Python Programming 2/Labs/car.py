# Gregory Campbell  lab10-2     February 22, 2022
"""
    This class holds data that models a car. It has the following attributes:
    __year_model for the car's year model, __make for the make of the car, and
    __speed for the car's current speed. It has an __init__ method that accepts
    the car's year model and make as arguments and assigns the initial speed of 
    the car. It has three methods: accelerate, which adds 5 to the speed attribute,
    brake, which subtracts 5 from the speed attribute, and get_speed, which returns
    the current speed of the car.
"""
class Car():
    # the __init__ method initializes a car object, setting speed to 0
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # the accelerate method adds 5 to the speed attribute when called
    def accelerate(self):
        self.__speed += 5

    # the brake method subtracts 5 from the speed attribute when called
    def brake(self):
        self.__speed -= 5

    # the get_speed method returns the car's current speed
    def get_speed(self):
        return self.__speed

    