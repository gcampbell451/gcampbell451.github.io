/**
   The RoomDemo class reads information about rooms from a file, creates Room objects for each of the rooms
   contained in the files, stores these Room objects in an ArrayList, and then displays all the information
   about the rooms using the appropriate methods of the Room class. Finally, the program displays the number 
   of rooms with each level of shade.
*/
import java.io.*;    // Needed for error handling, file IO
import java.util.*;  // Needed to create Scanner object

public class RoomDemo
{
   public static void main(String[] args)
   {
      // begin try block to handle errors
      try
      {
         // create file object, pass text file into constructor
         File file = new File("tuition.txt");
          
         // pass a reference to the File object as an argument to the Scanner class constructor                             
         Scanner inputFile = new Scanner(file);   
      
         // Declare and initialize local variables
         String name = "";
         double len = 0;
         double w = 0;
         int userChoice = 0;
         String shade = "";
         
         // create an array list to store Room objects. 
         ArrayList<Room> rooms = new ArrayList<Room>();
         
         // use loop to read contents of file
         while (inputFile.hasNext())
         {
            name = inputFile.nextLine();
            len = inputFile.nexDouble();
            w = inputFile.nextDouble();
         }
         
      
         // Get user input
         System.out.print("Please enter the name of the room: ");
         name = keyboard.nextLine();
         System.out.print("\nPlease enter the length of the room (in feet): ");
         len = keyboard.nextDouble();
         System.out.print("\nPlease enter the width of the room (in feet): ");
         w = keyboard.nextDouble();
         System.out.print("\nWhat is the amount of shade that this room receives?\n\n\t1. Little Shade\n\t2. Moderate Shade\n\t3. Abundant Shade\n\nPlease select from the options above: ");
         userChoice = keyboard.nextInt();
      
         // Convert userChoice from int to String to pass into Constructor
         switch (userChoice)
         {
            case 1:
               shade = "Little";
               break;
            case 2:
               shade = "Moderate";
               break;
            case 3:
               shade = "Abundant";
               break;
         }
         
         // Create an instance of the Room class
         Room project1Room = new Room(name, len, w, shade);
         
         // Display output
         System.out.printf("\nRoom Name: %s", project1Room.getRoomName());
         System.out.printf("\n\nRoom Area (in square feet): %,.1f", project1Room.calcArea());
         System.out.printf("\n\nAmount of Shade: %s", project1Room.getShadeAmount());
         System.out.printf("\n\nBTUs Per Hour needed: %,.0f", project1Room.calcRequiredCoolingCapacity());
      } //end of try
      
      // handle any errors
      catch(IOException ex)
      {
         System.out.println("Something went wrong reading the file: " + ex.getMessage());
      }
      
      
   }//end of main
}//end of class