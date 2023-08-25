import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.IOException;

public class RoomDemo2
{
   public static void main(String[] args) throws IOException
   {
      final int LITTLE_SHADE = 1;
      final int MODERATE_SHADE = 2;
      final int ABUNDANT_SHADE = 3;
   
      String name;
      double length, width;
      String shade = "";
      int littleShade = 0, moderateShade = 0, abundantShade = 0;
      
      //declare an ArrayList to hold all of our Room objects we will create
      ArrayList<Room> roomList = new ArrayList<Room>();
      
      try 
      {
         //create a File object that will be used to read the info from the file
         File file = new File("Rooms.txt");
         Scanner inputFile = new Scanner(file);
      
         //use a loop to read information from the file until there is no information left      
         while(inputFile.hasNext())
         {
            name = inputFile.nextLine();
            length = inputFile.nextDouble();
            width = inputFile.nextDouble();
            inputFile.nextLine();
            shade = inputFile.nextLine();
            if(inputFile.hasNext())
               inputFile.nextLine();
         
         //create a new Room object and add it to our ArrayList
            Room myRoom = new Room(name, length, width, shade);
            roomList.add(myRoom);
         }
      
         //use an enhanced for-loop to iterate over our ArrayList of Room objects and print out the information for each one
         //refer to "Using the Enhanced for Loop with an ArrayList" subsection in Chapter 7 Section 13
         for(Room myRoom : roomList)
         {
            System.out.println("Room Name: " + myRoom.getName());
            System.out.printf("Room Area: %,.1f\n", myRoom.getArea());
            System.out.println("Amount of Shade: " + myRoom.getShadeAmount());
            System.out.printf("BTUs Per Hour needed: %,.0f\n\n", myRoom.getCoolingCapacityNeeded());
         
            //keep track of the number of rooms with each type of shade amount
            if(myRoom.getShadeAmount().equalsIgnoreCase("Little"))
               littleShade++;
            else if(myRoom.getShadeAmount().equalsIgnoreCase("Moderate"))
               moderateShade++;
            else
               abundantShade++;
         }
         /*
         //You can also accomplish this using a standard for-loop
         for(int i = 0; i < roomList.size(); i++)
         {
            Room myRoom = roomList.get(i);
            System.out.println("Room Name: " + myRoom.getName());
            System.out.printf("Room Area: %,.1f\n", myRoom.getArea());
            System.out.println("Amount of Shade: " + myRoom.getShadeAmount());
            System.out.printf("BTUs Per Hour needed: %,.0f\n\n", myRoom.getCoolingCapacityNeeded());
            
            //keep track of the number of rooms with each type of shade amount
            if(myRoom.getShadeAmount().equalsIgnoreCase("Little"))
               littleShade++;
            else if(myRoom.getShadeAmount().equalsIgnoreCase("Moderate"))
               moderateShade++;
            else if(myRoom.getShadeAmount().equalsIgnoreCase("Abundant"))
               abundantShade++;
         }
         */
         System.out.println();
         System.out.println("Number of rooms with little shade: " + littleShade);
         System.out.println("Number of rooms with moderate shade: " + moderateShade);
         System.out.println("Number of rooms with abundant shade: " + abundantShade);
      
      }//close the "try" block of code
      catch(IOException ex)//If something goes wrong, an IOException is "thrown" to us, and we "catch" it and deal with it
      {
         //use the getMessage method of the exception we "caught" to print out it's message about what went wrong
         System.out.println("Something went wrong reading the file: " + ex.getMessage());
      }
   }
}