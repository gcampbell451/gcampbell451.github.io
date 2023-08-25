public class Building
{
   private String address;
   private double size;
   
   /**
   no-arg constructor
   */
   public Building()
   {
      address = "";
      size = 0;
   }
   
   /**
   Constructor for Building class
   @param address The street address of the building
   @param size The size of the building in square feet
   */
   public Building(String address, double size)
   {
      this.address = address;
      this.size = size;
   }
   
   /**
   Copy Constructor
   @param b a Building object to be copied
   */
   public Building(Building b)
   {
      this.address = b.address;
      this.size = b.size;
   }
   
   /**
   @return the street address of the building
   */
   public String getAddress()
   {
      return address;
   }
   
   /**
   @return the size (in square feet) of the building
   */
   public double getSize()
   {
      return size;
   }
   
   /**
   @param address the street address of the building
   */
   public void setAddress(String address)
   {
      this.address = address;
   }
   
   /**
   @param size the size (in square feet) of the building
   */
   public void setSize(double size)
   {
      this.size = size;
   }
  
   /**
   @return a String representation of the Building object
   */
   public String toString()
   {
      return String.format("Building Address: " + address +
                           "\nBuilding Size: %,.2f square feet", size);
   }
}