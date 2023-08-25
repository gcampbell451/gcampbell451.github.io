import java.util.*;
public class ParcelDemo
{
   public static void main(String[] args)
   {
      double buildingSize, parcelSize, totalPropertyTax = 0;
      int parcelID, zoning;
      String address, zoningType;
      char keepGoing;
      ArrayList<LandParcel> parcelList = new ArrayList<LandParcel>();
      
      Scanner keyboard = new Scanner(System.in);
      
      //continue to let the user enter information about Building and LandParcel objects until they indicate they wish to quit
      do
      {
         System.out.print("Please enter the Street Address of the Building: ");
         address = keyboard.nextLine();
      
         System.out.print("Please enter the size of the building (in square feet): ");
         buildingSize = keyboard.nextDouble();
      
         while(buildingSize < 0)//validate the input
         {
            System.out.print("Building size must be non-negative.  Please enter the size of the building (in square feet): ");
            buildingSize = keyboard.nextDouble();
         }
      
         System.out.print("Please enter the Parcel ID: ");
         parcelID = keyboard.nextInt();
      
         System.out.print("Please enter the size of the parcel (in acres): ");
         parcelSize = keyboard.nextDouble();
      
         while (parcelSize < 0)//validate the input
         {
            System.out.print("Parcel size must be non-negative.  Please enter the size of the parcel (in acres): ");
            parcelSize = keyboard.nextDouble();
         }
      
         System.out.print("Enter 1 for Commercial Zoning or 2 for Residential Zoning: ");
         zoning = keyboard.nextInt();
      
         while(zoning != 1 && zoning != 2)//validate the input
         {
            System.out.print("Invalid Selection.  Enter 1 for Commercial Zoning or 2 for Residential Zoning: ");
            zoning = keyboard.nextInt();
         }
      
         //assign zoning based on menu selection above
         if(zoning == 1)
            zoningType = "Commercial";
         else
            zoningType = "Residential";
         
         Building b = new Building(address, buildingSize);//instantiate Building object
         LandParcel p = new LandParcel(parcelID, parcelSize, zoningType, b);//instantiate LandParcel object
         totalPropertyTax += p.getPropertyTax();//add to our running total of property taxes
         parcelList.add(p);//add LandParcel object to ArrayList
         
         keyboard.nextLine();
         System.out.print("\nWould you like to enter information about another parcel (Y/N)?");
         keepGoing = keyboard.nextLine().toUpperCase().charAt(0);
         System.out.println();
      }
      while(keepGoing == 'Y');
      
      //iterate over the ArrayList and print out information about each LandParcel
      for(int i = 0; i <parcelList.size(); i++)
      {
         System.out.println(parcelList.get(i));//implicitly calling to LandParcel's toString()
         System.out.println();
      }
      
      //print out the average property taxes
      System.out.printf("The average property taxes are: $%,.2f",totalPropertyTax/parcelList.size());
   }
}