import java.util.Scanner;
public class Exam2Campbell {
   public static void main(String[] args) {
      // Declare and initialize input variables
      int taxiType = 0;       // Type of taxi used
      double distance = 0;    // Distance to destination
      int numStops = 0;       // Number of stops made
      int numCustomers = 0;   // Number of customers serviced
      
      // Declare and initialize processing variables
      double perMileFee = 0;
      double baseFee = 0;
      double totalFee = 0;
      double grandTotal = 0;
      
      // Print title, create scanner object for user entry
      System.out.println("CPCC Taxi Service");
      Scanner keyboard = new Scanner(System.in);
      
      // Ask for number of customers
      System.out.print("\nHow many customers did this cab service during this shift? ");
      numCustomers = keyboard.nextInt();      
      
      // Create for loop for numCustomers
      for (int i = 0; i < numCustomers; i++) {
         // Call method to display taxi type menu
         displayMenu();
         
         // Ask user for taxi type, validate entry
         System.out.print("Please select the type of taxi from the menu: ");
         taxiType = keyboard.nextInt();
         
         while (taxiType < 1 || taxiType > 3) {
            System.out.print("Invalid input! Please enter a number between 1 and 3.\n\n");
            System.out.print("Please select the type of taxi from the menu: ");
            taxiType = keyboard.nextInt();
         }
         
         // Ask user for distance, validate entry
         System.out.print("Please enter the distance traveled in miles for customer " + (i + 1) + ": ");
         distance = keyboard.nextDouble();
         
         while (distance < 0) {
            System.out.print("Invalid input! Please enter a nonzero number.\n\n");
            System.out.print("Please enter the distance traveled in miles for customer " + (i + 1) + ": ");
            distance = keyboard.nextDouble();
         }
         
         // Ask user for number of stops, validate entry
         System.out.print("Please enter the number of stops for customer " + (i + 1) + ": ");
         numStops = keyboard.nextInt();
         
         while (numStops < 0) {
            System.out.print("Invalid input! Please enter a nonzero number.\n\n");
            System.out.print("Please enter the number of stops for customer " + (i + 1) + ": ");
            numStops = keyboard.nextInt();
         }
         
         // Call fee methods
         perMileFee = calcPerMileFee(taxiType);
         baseFee = calcBaseFee(distance, perMileFee);
         totalFee = calcTotalFee(baseFee, numStops);
         
         // Call method to display taxi fee
         displayTaxiFee(totalFee); 
         
         // Aggregate totalFees
         grandTotal += totalFee;
      }       
      
      // Print grand total
      System.out.printf("\nThe total of all Taxi Fees is $%,.2f", grandTotal);
   }
   
   /**
      This method displays the Taxi Type Menu
   */
   public static void displayMenu() {
      System.out.println("\nTaxi Type Menu");
      System.out.print("\n\t1. Standard\n\t2. Business\n\t3. Luxury\n\n");
   }
   
   /**
      This method calculates the fee per mile
      @param taxi type is the type of taxi used
      @return perMileFee is the fee per mile based on the type of taxi
   */
   public static double calcPerMileFee(int taxiType) {
      // Declare and initialize return variable
      double perMileFee = 0;
      
      // Declare and intitialize constant prices
      final double STANDARD_TAXI = 1.50;
      final double BUSINESS_TAXI = 2.00;
      final double LUXURY_TAXI = 2.50;
      
      // Create switch to determine fee
      switch (taxiType) {
         case 1: 
            perMileFee = STANDARD_TAXI;
            break;
         case 2:
            perMileFee = BUSINESS_TAXI;
            break;
         default:
            perMileFee = LUXURY_TAXI;
            break;         
      }
      return perMileFee;
   }
   
   /**
      This method calculates the base fee
      @param distance is the distance to the destination
      @param perMileFee is the fee per mile based on the type of taxi
      @return baseFee is the fee based on distance and taxi type 
   */
   public static double calcBaseFee(double distance, double perMileFee) {
      // Declare and initialize return variable
      double baseFee = 0;
      
      // Calculate base fee
      baseFee = distance * perMileFee;
      
      return baseFee;
   }
   
   /**
      This method calculates the total fee per customer
      @param baseFee is the fee based on distance and taxi type
      @param numStops is the number of stops made on the trip
      @return totalFee is the total fee per customer
   */
   public static double calcTotalFee(double baseFee, int numStops) {
      // Declare and initialize return variable
      double totalFee = 0;
      
      // Calculate total fee
      totalFee = baseFee + (5.00 * numStops);
      
      return totalFee;
   }
   
   /**
      This method displays the taxi fee
      @param totalFee is the total fee per customer
   */
   
   public static void displayTaxiFee(double totalFee) {
      System.out.printf("Taxi Fee: $%,.2f\n", totalFee);
   }
}