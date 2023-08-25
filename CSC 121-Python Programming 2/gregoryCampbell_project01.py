# Gregory Campbell  Project 1   September 11, 2021
"""
This program asks the user for the length and width of a room and the amount of shade
the room receives. It calculates the area and determines, based on the square footage 
and shade, how much cooling, in BTUs per hour, must be used to properly cool the room. 
It then displays a greeting, the area of the room, the amount of shade received, and 
the amount of cooling needed.

"""

#============= Constants

LESS_THAN_250 = 5500                # These map square footage to amount of cooling needed in BTUs
FROM_250_TO_500 = 10000
FROM_501_TO_1000 = 17500
OVER_1000 = 24000

LITTLE_SHADE_ADJUSTMENT = .15       # These scalars map adjustments to cooling needed based
ABUNDANT_SHADE_ADJUSTMENT = .10     # on amount of shade received

#============= Input Variables

length = 0                          # These store user inputs
width = 0
userChoice = 0

#============= Processing Variables

area = 0                            # This stores the calculated area of the room
shadeAmount = ""                    # This stores a string for display of user choice
btusNeeded = 0                      # This stores the amount of cooling needed

#============= Get dimensions of room

length = float(input("Please enter the length of the room (in feet): "))
width = float(input("Please enter the width of the room (in feet): "))

#============= Calculate area of room

area = length * width

#============= Display menu that asks user how much shade the room gets

userChoice = int(input('What is the amount of shade that this room receives?\n\n\t1. Little Shade\n\n\t' +
                        '2. Moderate Shade\n\n\t3.Abundant Shade\n\nPlease select from the options above: '))

#============ Convert userChoice to a string for future display

if userChoice == 1:
    shadeAmount = "Little"
elif userChoice == 2:
    shadeAmount = "Moderate"
else:
    shadeAmount = "Abundant"
    
#============= Determine capacity of AC unit needed

if area < 250:
    btusNeeded = LESS_THAN_250
elif area <= 500:
    btusNeeded = FROM_250_TO_500
elif area <= 1000:
    btusNeeded = FROM_501_TO_1000
else:
    btusNeeded = OVER_1000
    
#============= Adjust for amount of shade received

if shadeAmount == "Little":
    btusNeeded += (btusNeeded * LITTLE_SHADE_ADJUSTMENT)
elif shadeAmount == "Abundant":
    btusNeeded -= (btusNeeded * ABUNDANT_SHADE_ADJUSTMENT)
    
#============= Create String object for greeting

greeting = "\nAir Conditioning Window Unit Cooling Capacity\n"  

#============= Display output
    
print(greeting)
print("Room Area (in square feet):",area, "\n")    
print("Amount of Shade:",shadeAmount, "\n")
print(f'BTU\'s Per Hour needed: {btusNeeded:,.0f}')

