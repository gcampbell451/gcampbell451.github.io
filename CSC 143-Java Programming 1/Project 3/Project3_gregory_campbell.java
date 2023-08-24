import java.util.Scanner;  // Needed for scanner class

public class Project3_gregory_campbell {
   public static void main(String[] args) { 
      
      // Declare input variables
      String roomName = "";                  // Store name of room
      double roomLength = 0;                 // Length of room in feet
      double roomWidth = 0;                  // Width of room in feet
      int shadeAmount = 0;                   // Store user selection from menu
      
      // Declare processing variables

      String shadeType = "";                 // Used to convert user input from menu to desired output
      double roomArea = 0;                   // Holds the area of the room in square feet
      double totalCapacity = 0;              // Create return variable to store adjusted BTU needs
      int numRooms = 0;                      // Store number of rooms user entered information for
      String answer;                         // Store whether user wants to continue
      
      // Create scanner object
      Scanner keyboard = new Scanner(System.in);
      
      // Begin do while loop
      do {
      
         // Ask user to enter the name of the room
         System.out.print("\nPlease enter the name of the room: ");
         roomName = keyboard.nextLine();
         
         // Ask user to enter length of room in feet
         System.out.print("Please enter the length of the room (in feet): ");
         roomLength = keyboard.nextDouble();
         
         // Validate that the length of the room is < 5 feet
         while (roomLength < 5) {
            System.out.print("\nInvalid input! The length cannot be less than 5 feet!");
            System.out.print("\nPlease enter the length of the room (in feet): ");
            roomLength = keyboard.nextDouble();
         }
         
         // Ask user to enter width of room in feet
         System.out.print("Please enter the width of the room (in feet): ");
         roomWidth = keyboard.nextDouble();
         
         // Validate that the width of the room is < 5 feet
         while (roomWidth < 5) {
            System.out.print("\nInvalid input! The width cannot be less than 5 feet!");
            System.out.print("\nPlease enter the width of the room (in feet): ");
            roomWidth = keyboard.nextDouble();
         }
         
         // Display a menu that asks user how much shade the room gets
         System.out.println("What is the amount of shade that this room receives?\n\n\t 1. Little Shade\n\t 2. Moderate Shade\n\t 3. Abundant Shade\n");
         System.out.print("Please select from the options above: ");
         shadeAmount = keyboard.nextInt();
         
         // Validate that the user entered a correct option
         while (shadeAmount < 1 || shadeAmount > 3) {
            System.out.println("\nInvalid input! Please enter 1, 2, or 3.");
            System.out.println("What is the amount of shade that this room receives?\n\n\t 1. Little Shade\n\t 2. Moderate Shade\n\t 3. Abundant Shade\n");
            System.out.print("Please select from the options above: ");
            shadeAmount = keyboard.nextInt();
         }
         
         // Clear scanner buffer
         keyboard.nextLine(); 
         
         // Call displayTitle method
         displayTitle();
         
         // Call calculateArea method
         roomArea = calculateArea(roomLength, roomWidth);
         
         // Call translasteShadeChoiceToString method
         shadeType = translateShadeChoiceToString(shadeAmount);
         
         // Call calculateBTUsPerHour method
         totalCapacity = calculateBTUsPerHour(roomArea, shadeAmount);
         
         // Call displayRoomInformation method
         displayRoomInformation(roomName, roomArea, shadeType, totalCapacity);       
                  
         // Update number of rooms information has been entered for
         numRooms++;        
                 
         // Ask user if they want to enter information about another room
         System.out.print("\n\nWould you like to enter information for another room(Y/N)? ");
         answer = keyboard.nextLine();
         answer = answer.toLowerCase();      
      
      } while (answer.equals("y") || answer.equals("yes"));
      
      // Print goodbye message
      System.out.printf("\nThe total number of rooms processed was: %d", numRooms);
   }
   /**
      This method displays the company title
   */
   public static void displayTitle() {
      // Store company title in a variable
      String outputHeader = "\nAir Conditioning Window Unit Cooling Capacity\n";
      
      System.out.print(outputHeader);
      
   }
   /**
      This method accepts the length and width of a room as arguments, and calculates and returns the area of the room
      @param roomLength is the length of the room in feet
      @param roomWidth is the width of the room in feet
      @return roomArea returns the area of the room in square feet
   */
   public static double calculateArea(double roomLength, double roomWidth) {
      double roomArea = roomLength * roomWidth;
      return roomArea;
   }
   /**
      This method accepts an integer value (1, 2, or 3) that denotes the amount of shade. It returns the appropriate String representation of the shade
      @param shadeAmount holds the user entry corresponding to the amount of shade the room receives
      @return shadeType returns the String representation to main
   */
   public static String translateShadeChoiceToString(int shadeAmount) {
      String shadeType = "";                 // Declare and initialize return variable
      switch (shadeAmount)                   // Use swich to adjust for shade
      {
         case 1:
            shadeType = "Little";
            break;
         case 3:
            shadeType = "Abundant";
            break;
         default:
            shadeType = "Moderate";
            break;
      }
      return shadeType;   
   }
   /**
      This method accepts the area of a room and the amount of shade a room gets and returns the BTUs per Hour that are needed to adequately cool that room
      @param roomArea is the area of the room in square feet
      @param shadeAmount holds the user entry corresponding to the amount of shade the room receives
      @return totalCapacity returns the BTUs per hour needed to cool the room
   */
   public static double calculateBTUsPerHour(double roomArea, int shadeAmount) {
      // Declare constant variables
      final double ROOM_UNDER_250 = 5500;    // Store capacities for specific room sizes
      final double ROOM_TO_500 = 10000;
      final double ROOM_UNDER_1000 = 17500;
      final double ROOM_1000_PLUS = 24000;
      final double LITTLE_SHADE = .15;       // Store adjustments based on shade amount
      final double LOTTA_SHADE = .10;
      double adjustForShade = 0;             // Create variable to adjust capacity based on shade amount 
      double capacity = 0;                   // Store variable for AC Capacity based on room size
      double totalCapacity = 0;              // Create return variable to store adjusted BTU needs
      
      // Determine capacity needed for moderately shaded room, adust for shade
      if (roomArea < 250)
         capacity = ROOM_UNDER_250;          // Determine capacity based on room size
      else if (roomArea <= 500)
         capacity = ROOM_TO_500;
      else if (roomArea < 1000)
          capacity  = ROOM_UNDER_1000;
      else capacity = ROOM_1000_PLUS;
      
      switch (shadeAmount)                   // Use swich to adjust for shade
      {
         case 1:
            adjustForShade = capacity * LITTLE_SHADE;
            totalCapacity = capacity + adjustForShade;
            break;
         case 3:
            adjustForShade = capacity * LOTTA_SHADE;
            totalCapacity = capacity - adjustForShade;
            break;
         default:
            totalCapacity = capacity;
            break;
      }
      return totalCapacity;    
   }
   /**
      This method prints out the information for a single room
      @param roomName holds the name of the room
      @param roomArea holds the area of the room in square feet
      @param shadeType holds the holds the String representation corresponding to the amount of shade the room receives
      @param totalCapacity holds the BTUs per hour needed to cool the room
   */
   public static void displayRoomInformation(String roomName, double roomArea, String shadeType, double totalCapacity) {
      // Display name of room, area of room, amount of shade, total capacity.
      System.out.printf("\nRoom Name: %s\n", roomName);
      System.out.printf("Room Area(in square feet): %.1f\n", roomArea);
      System.out.printf("Amount of Shade: %s\n", shadeType);
      System.out.printf("BTU's Per Hour needed: %,.0f", totalCapacity);      
   }
}