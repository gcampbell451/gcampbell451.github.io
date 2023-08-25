# Gregory Campbell  Project 2   October 22, 2021
"""
This program asks the user for the length and width of a room and the amount of shade
the room receives. It calculates the area and determines, based on the square footage 
and shade, how much cooling, in BTUs per hour, must be used to properly cool the room. 
It then displays a greeting, the area of the room, the amount of shade received, and 
the amount of cooling needed.

Modifications for project 2:
   add code to prompt the user to enter the name of the room they are entering information for
   add input validation:
       length >= 5 feet
       width >= 5 feet
       userChoice must be 1, 2, or 3
   add code to keep program running until user decides to quit
   after user quits, output number of rooms entered

"""

#============= Constants

LESS_THAN_250 = 5500                # These map square footage to amount of cooling needed in BTUs
FROM_250_TO_500 = 10000
FROM_501_TO_1000 = 17500
OVER_1000 = 24000

LITTLE_SHADE_ADJUSTMENT = .15       # These scalars map adjustments to cooling needed based
ABUNDANT_SHADE_ADJUSTMENT = .10     # on amount of shade received

#============= Input Variables

roomName = ""                       # These store user inputs
length = 0                          
width = 0
userChoice = 0

#============= Processing Variables

area = 0                            # This stores the calculated area of the room
shadeAmount = ""                    # This stores a string for display of user choice
btusNeeded = 0                      # This stores the amount of cooling needed
keepGoing = "Y"                     # initialize variable to keep loop running until user quits
count = 0                           # initialize variable to keep count of rooms processed

# begin loop to keep program running
while keepGoing == "Y" or keepGoing == "y":

     #============= Get user input

     roomName = input("\nPlease enter the name of the room: ")
     length = float(input("Please enter the length of the room (in feet): "))
     
     # validate input
     while length < 5:
          print("\nThe length of the room cannot be less than 5 feet.")
          length = float(input("\nPlease enter the length of the room (in feet): "))
          
     width = float(input("Please enter the width of the room (in feet): "))
     
     # validate input
     while width < 5:
          print("\nThe width of the room cannot be less than 5 feet.")
          width = float(input("\nPlease enter the width of the room (in feet): "))          

     #============= Calculate area of room
     
     area = length * width
     
     #============= Display menu that asks user how much shade the room gets
     
     userChoice = int(input('\nWhat is the amount of shade that this room receives?\n\n\t1. Little Shade\n\n\t' +
                             '2. Moderate Shade\n\n\t3.Abundant Shade\n\nPlease select from the options above: '))
     
     while userChoice < 1 or userChoice > 3:
          print("\nInvalid input. Please enter 1, 2, or 3")
          userChoice = int(input('\nWhat is the amount of shade that this room receives?\n\n\t1. Little Shade\n\n\t' +
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
     print(f'Room Name: {roomName}')
     print(f'Room Area (in square feet): {area:,.1f}')    
     print(f'Amount of shade: {shadeAmount}')
     print(f'BTU\'s Per Hour needed: {btusNeeded:,.0f}')
     
     #============= Increment count
     count += 1
     
     #============= ask user to continue or quit
     keepGoing = input("\nWould you like to enter information for another room (Y/N)? ")

#================== print number of rooms processed
print(f'\nThe total number of rooms processed was: {count}')