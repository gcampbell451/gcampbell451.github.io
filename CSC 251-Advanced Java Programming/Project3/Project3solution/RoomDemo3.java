import java.util.Scanner;
import java.util.ArrayList;
import java.io.File;
import java.io.IOException;

public class RoomDemo3
{
   public static void main(String[] args) throws IOException
   {
      final int LITTLE_SHADE = 1;
      final int MODERATE_SHADE = 2;
      final int ABUNDANT_SHADE = 3;
      
      String name;
      double length, width;
      String shade = "";
      String manufacturer, type;
      double acCoolingCapacity;
      
      //declare an ArrayList to hold all of our Room objects we will create
      ArrayList<Room> roomList = new ArrayList<Room>();
      
      try 
      {
         //create a File object that will be used to read the info from the file
         File file = new File("Rooms2.txt");
         Scanner inputFile = new Scanner(file);
      
         //use a loop to read information from the file until there is no information left       
         while(inputFile.hasNext())
         {
            name = inputFile.nextLine();
            length = inputFile.nextDouble();
            width = inputFile.nextDouble();
            inputFile.nextLine();
            shade = inputFile.nextLine();
            manufacturer = inputFile.nextLine();
            type = inputFile.nextLine();
            acCoolingCapacity = inputFile.nextDouble();
            if(inputFile.hasNext())
               inputFile.nextLine();//clear the newline left in the buffer after calling nextDouble()
            if(inputFile.hasNext())
               inputFile.nextLine();//skip the blank line between Rooms in the file
         
            //Here we do a few things:
            //We first create a new AirConditioner object that is passed as one of the arguments to
            //create a new Room object, which is then added to our ArrayList
            roomList.add(new Room(name, length, width, shade, new AirConditioner(manufacturer, type, acCoolingCapacity)));
         }
      
         //use a for loop to iterate over our ArrayList of Room objects and print out the information for each one
         //by implicitly calling the toString() method
         for(Room myRoom : roomList)
         {
            System.out.println(myRoom);
            System.out.println();
         }
         /*
         //You can also accomplish this using a standard for-loop
         for(int i = 0; i < roomList.size(); i++)
         {
            Room myRoom = roomList.get(i);
            System.out.println(myRoom);
            System.out.println();
         }
         */
      }//close the "try" block of code
      catch(IOException ex)//If something goes wrong, an IOException is "thrown" to us, and we "catch" it and deal with it
      {
         //use the getMessage method of the exception we "caught" to print out it's message about what went wrong
         System.out.println("Something went wrong reading the file: " + ex.getMessage());
      }
   }
}