import java.util.Scanner;
import java.util.ArrayList;

public class DemoCampbell
{
   public static void main(String[] args)
   {
      // declare and initialize constants for ratings
      final String EXCELLENT = "Excellent";
      final String GOOD = "Good";
      final String UNACCEPTABLE = "Unacceptable";
  
      // declare and initialize variable to allow user to continue or quit
      String keepGoing = "Y";
      
      // declare and initialize input variables
      String name = "";
      double totalWidgets = 0;
      double rejectedWidgets = 0;
      
      // declare and initialize processing variables
      double total = 0;       //  accumulator for quality
      double efficiency = 0;
      String rating = "";
      
      // create AssemblyLine object that expands as objects are added
      ArrayList<AssemblyLine> demoList = new ArrayList<>();
      
      // begin program loop
      do
      {
         // create Scanner object for user input
         Scanner keyboard = new Scanner(System.in);
         
         // get user input
         System.out.print("\n\nEnter the name of the assembly line: ");
         name = keyboard.nextLine();
         
         System.out.print("\nEnter the total number of widgets manufactured: ");
         totalWidgets = keyboard.nextInt();
         keyboard.nextLine();    // consume nextLine
         
         System.out.print("\nEnter the number of rejected widgets manufactured: ");
         rejectedWidgets = keyboard.nextInt();
         keyboard.nextLine();
         
         // create AssemblyLine object containing user input, add object to list
         demoList.add(new AssemblyLine(name, totalWidgets, rejectedWidgets));
         
         // ask user to continue or quit
         System.out.print("\n\nDo you want to enter information for another line? (Y/N) ");
         keepGoing = keyboard.nextLine();
         
      } while (keepGoing.equalsIgnoreCase("Y"));
      
      // Display output
      System.out.println("\n\nQuality Report:\n");
      
      // loop through ArrayList to display line name and calculated quality
      for (int i = 0; i < demoList.size(); i++)
      {     
         
         
         AssemblyLine output = demoList.get(i);    // create AssemblyLine object to facilitate output
         System.out.println("\nAssembly Line: " + output.getName());
         System.out.printf("\nQuality (as a percentage): %.2f\n\n", output.calcAssemblyLineQuality());
         
         total += output.calcAssemblyLineQuality();   // accumulate line quality for efficiency calculation
      }
      
      // calculate efficiency, rating based on given formula, table
      efficiency = total / demoList.size();
      
      if (efficiency > 95.00)
      {
         rating = EXCELLENT;
      } 
      else if (efficiency >= 90.00)
      {
         rating = GOOD;
      }
      else
      {
         rating = UNACCEPTABLE;
      }
      
      System.out.println("\nThe efficiency of the factory is: " + rating);
   
   }// end of main
   
 
   
   
}// end of class