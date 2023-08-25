public class Building
{
   // instance fields
   private String address;
   private double sqFootage;
   
   // no-arg
   public Building()
   {
      address = "";
      sqFootage = 0.0;
   }
   
   // constructor that accepts args
   public Building(String address, double sqFootage)
   {
      this.address = address;
      this.sqFootage = sqFootage;
   }
   
   // copy constructor
   public Building(Building obj2)
   {
      this.address = obj2.address;
      this.sqFootage = obj2.sqFootage;
   }
   
   // muatators
   public void setAddress(String address)
   {
      this.address = address;
   }
   
   public void setSqFootage(double sqFootage)
   {
      this.sqFootage = sqFootage;
   }
   
   // accessors
   public String getAddress()
   {
      return address;
   }
   
   public double getSqFootage()
   {
      return sqFootage;
   }
   
   // toString
   public String toString()
   {
      return String.format("Address: " + address + "\nSquare Footage: %,.2f\n", sqFootage);
   }
}