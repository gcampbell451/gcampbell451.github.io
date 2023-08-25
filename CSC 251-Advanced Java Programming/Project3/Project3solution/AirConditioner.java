public class AirConditioner
{
   //fields
   private String manufacturer;
   private String type;
   private double coolingCapacity;
   
   //no-arg constructor
   public AirConditioner()
   {
      manufacturer = "";
      type = "";
      coolingCapacity = 0;
   }
   
   //constructor that accepts arguments
   public AirConditioner(String manufacturer, String type, double coolingCapacity)
   {
      this.manufacturer = manufacturer;
      this.type = type;
      this.coolingCapacity = coolingCapacity;
   }
   
   //copy constructor
   public AirConditioner(AirConditioner ac)
   {
      this.manufacturer = ac.manufacturer;
      this.type = ac.type;
      this.coolingCapacity = ac.coolingCapacity;
   }
   
   //setters
   public void setManufacturer(String manufacturer)
   {
      this.manufacturer = manufacturer;
   }
   
   public void setType(String type)
   {
      this.type = type;
   }
   
   public void setCoolingCapacity(double coolingCapacity)
   {
      this.coolingCapacity = coolingCapacity;
   }
   
   //getters
   public String getManufacturer()
   {
      return manufacturer;
   }
   
   public String getType()
   {
      return type;
   }
   
   public double getCoolingCapacity()
   {
      return coolingCapacity;
   }
   
   /**
   The toString method returns a string representation of our AirConditioner object
   */
   public String toString()
   {
      return String.format("Air Conditioner Manufacturer: " + manufacturer +
             "\nAir Conditioner Type: " + type +
             "\nAir Conditioner Cooling Capacity (BTUs Per Hour): %,.0f\n", coolingCapacity);
   }
}