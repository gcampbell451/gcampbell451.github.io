import java.util.Scanner;
public class Chap3ProgChallenge7    // 7.Sorted Names
{
   public static void main(String[] args)
   {
      // Create Scanner object for user input
      Scanner keyboard = new Scanner(System.in);
      
      // Initialize string variables
      String name1 = "";
      String name2 = "";
      String name3 = "";
      
      // Get user input   
      System.out.print("Enter a person's name: ");
      name1 = keyboard.nextLine();
      
      System.out.print("Enter another person's name: ");
      name2 = keyboard.nextLine();
      
      System.out.print("Enter another person's name: ");
      name3 = keyboard.nextLine();
          
      System.out.print("Those names in alphabetical order are:\n");
      
      // Compare names and print output
      if ((name1.compareTo(name2) < 0) && (name2.compareTo(name3) < 0))          // I put the six possible combinations of the order
         System.out.printf("%-10s\n %-10s\n %-10s", name1, name2, name3);        // of names into the print statements and used those
      else if ((name3.compareTo(name1) < 0) && (name1.compareTo(name2) < 0))     // orders to create the comparison operations.
         System.out.printf("%-10s\n %-10s\n %-10s", name3, name1, name2);
      else if ((name3.compareTo(name2) < 0) && (name2.compareTo(name1) < 0))
         System.out.printf("%-10s\n %-10s\n %-10s", name3, name2, name1);
      else if ((name2.compareTo(name1) < 0) && (name1.compareTo(name3) < 0))
         System.out.printf("%-10s\n %-10s\n %-10s", name2, name1, name3);
      else if ((name2.compareTo(name3) < 0) && (name3.compareTo(name1) < 0))
         System.out.printf("%-10s\n %-10s\n %-10s", name2, name3, name1);
      else  
         System.out.printf("%-10s\n %-10s\n %-10s", name1, name3, name2);
      
      
   }
}