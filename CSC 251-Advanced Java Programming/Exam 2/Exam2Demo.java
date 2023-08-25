import java.util.Scanner;
import java.util.ArrayList;
public class Exam2Demo
{
   public static void main(String[] args)
   {
      // initialize variable to keep program running
      String keepGoing = "Y";
      
      // initialize variables to store user entries
      String idNum = "";
      double parcelSize = 0.0;
      String zoning = "";
      String address = "";
      double bldgSize = 0.0;
      
      // initialize variable to track tax, total tax, number of parcels, calculate average
      double tax = 0.0;
      double totalTax = 0.0;
      double average = 0.0;
      
      // create ArrayList to store Land objects
      ArrayList<Land> demoList = new ArrayList<>();
      
      // begin program loop
      do
      {
         // create Scanner for user input
         Scanner keyboard = new Scanner(System.in);
         
         // prompt user for input
         System.out.print("Enter the Parcel ID: ");
         idNum = keyboard.nextLine();
         
         System.out.print("Enter the parcel size in acres: ");
         parcelSize = keyboard.nextDouble();
         
         // validate
         while (parcelSize < 0)
         {
            System.out.println("Invalid input! Enter a non-negative number.");
            System.out.print("Enter the parcel size in acres: ");
            parcelSize = keyboard.nextDouble();
         }
         keyboard.nextLine();
         
         System.out.print("Enter the zoning type (Residential/Commercial): ");
         zoning = keyboard.nextLine();
         
         System.out.print("Enter the building's address: ");
         address = keyboard.nextLine();
         
         System.out.print("Enter the building size in square feet: ");
         bldgSize = keyboard.nextDouble();
         
         //validate
         while (bldgSize < 0)
         {
            System.out.println("Invalid input! Enter a non-negative number.");
            System.out.print("Enter the building size in square feet: ");
            bldgSize = keyboard.nextDouble();
         }
         keyboard.nextLine();
         
         // create Building object
         Building building = new Building(address, bldgSize);
         
         //create Land object
         Land land = new Land(idNum, parcelSize, zoning, building);
         
         // calculate tax
         tax = land.calcTax();
         
         // add Land object to ArrayList
         demoList.add(land);
         
         // aggregate tax
         totalTax += tax;
         
         // prompt user to continue or quit
         System.out.println("Do you have another parcel to enter(Y/N) ?: ");
         keepGoing = keyboard.nextLine();
         
      } while (keepGoing.equalsIgnoreCase("Y"));
      
      // calculate average tax
      average = totalTax / demoList.size();
      
      // print information
      for (Land parcel : demoList)
         System.out.println(parcel.toString());
 
      System.out.printf("Tha average property tax amount is $%,.2f.", average);
      
   }// endo main

}// endo class