public class Room
{
   //declare fields
   private String name;
   private double length;
   private double width;
   private String shadeAmount;
   private AirConditioner ac;
   //notice we don't have a field to hold the required cooling capacity
   //Since that value depends on the area of the room, it needs to be calculated each time it is needed
   //So we call getCoolingCapacityNeeded() to avoid getting stale data (See Section 6.2)

   //no-arg constructor
   public Room()
   {
      name = "";
      length = 0;
      width = 0;
      shadeAmount = "";
      ac = new AirConditioner();
   }
   
   //constructor that accepts arguments
   public Room(String name, double length, double width, String shadeAmount, AirConditioner ac)
   {
      this.name = name;
      this.length = length;
      this.width = width;
      this.shadeAmount = shadeAmount;
      this.ac = new AirConditioner(ac);//make a copy of the "ac" argument we are passed to avoid a security hole
   }

   //setters
   public void setName(String name)
   {
      this.name = name;
   }
   
   public void setShadeAmount(String shadeAmount)
   {
      this.shadeAmount = shadeAmount;
   }
   
   public void setLength(double length)
   {
      this.length = length;
   }
   
   public void setWidth(double width)
   {
      this.width = width;
   }      
   
   public void setAirConditioner(AirConditioner ac)
   {
      this.ac = new AirConditioner(ac);//make a copy of the "ac" argument we are passed to avoid a security hole
   }
   //getters
   public String getName()
   {
      return name;
   }
   
   public String getShadeAmount()
   {
      return shadeAmount;
   }
   
   public double getLength()
   {
      return length;
   }
   
   public double getWidth()
   {
      return width;
   }
   
   public AirConditioner getAirConditioner()
   {
      return new AirConditioner(ac);//return a copy of our AirConditioner object - avoids security holes
   }
   
   public double getArea()
   {
      return length * width;
   }
   
   /**
   Calculates and returns the cooling capacity needed to cool the room
   */
   public double getCoolingCapacityNeeded()
   {
      final double LITTLE_SHADE_PERCENTAGE = 1.15;
      final double ABUNDANT_SHADE_PERCENTAGE = .9;//Multiplying by .9 is the same as decreasing by 10%
      
      double btus = 0;
      
      if(getArea() < 250)
      {
         btus =  5500;
      }
      else if(getArea() <= 500)
      {
         btus =  10000;
      }
      else if(getArea() < 1000)
      {
         btus =  17500;
      }
      else//over 1000
      {
         btus =  24000;
      }
      
      if(getShadeAmount().equalsIgnoreCase("Little"))
         btus = btus * LITTLE_SHADE_PERCENTAGE;
      
      if(getShadeAmount().equalsIgnoreCase("Abundant"))
         btus = btus * ABUNDANT_SHADE_PERCENTAGE;
         
      return btus;
   }
   
   /**
   Checks the cooling required for the room and the cooling capacity of the
   AirConditioner object it has to see if the room is adequately cooled
   */
   public boolean hasAdequateCooling()
   {
      if( ac.getCoolingCapacity() >= getCoolingCapacityNeeded())
         return true;
      else
         return false;
   }
   
   /**
   The toString method returns a string representation of our Room object
   */
   public String toString()
   {
      return String.format("Room Name: " + name +
             "\nRoom Area: %,.1f" +
             "\nAmount of Shade: " + shadeAmount +
             "\nBTUs Per Hour needed: %,.0f" + 
             "\n" + ac + //we implicitly call the AirConditioner's toString method here
             "This room is" + (hasAdequateCooling() ? "" : " not") +  " adequately cooled", getArea(), getCoolingCapacityNeeded());
             //in the line above, we use the ternary operator to check the cooling to decide if we print "not" in front of "adequately cooled"
   }
}