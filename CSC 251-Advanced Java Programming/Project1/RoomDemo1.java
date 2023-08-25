import java.util.Scanner;

public class RoomDemo1
{
   public static void main(String[] args)
   {
      final int LITTLE_SHADE = 1;
      final int MODERATE_SHADE = 2;
      final int ABUNDANT_SHADE = 3;
   
      String name;
      double length, width;
      int shadeChoice;
      String shade = "";
      Scanner keyboard = new Scanner(System.in);
      
      System.out.print("Please enter the name of the room: ");
      name = keyboard.nextLine();
      
      System.out.print("Please enter the length of the room (in feet): ");
      length = keyboard.nextDouble();
      
      System.out.print("Please enter the width of the room (in feet): ");
      width = keyboard.nextDouble();
            
      System.out.println("What is the amount of shade that this room receives?");
      System.out.println("\t1. Little Shade");
      System.out.println("\t2. Moderate Shade");
      System.out.println("\t3. Abundant Shade");
      System.out.print("Please select from the options above: ");
      shadeChoice = keyboard.nextInt();
      
      if(shadeChoice == LITTLE_SHADE)
      {
         shade = "Little";
      }
      else if(shadeChoice == ABUNDANT_SHADE)   
      {
         shade = "Abundant";
      }
      else //we know it's moderate
      {
         shade = "Moderate";
      }
      
      //create our Room object by using the new keyword and calling the constructor that accepts arguments
      Room myRoom = new Room(name, length, width, shade);
      
      //use the accessor methods of the Room class to print out the information about our Room object
      System.out.println("Room Name: " + myRoom.getName());
      System.out.printf("Room Area: %,.1f\n", myRoom.getArea());
      System.out.println("Amount of Shade: " + myRoom.getShadeAmount());
      System.out.printf("BTUs Per Hour needed: %,.0f\n", myRoom.getCoolingCapacityNeeded()); 
   }
}