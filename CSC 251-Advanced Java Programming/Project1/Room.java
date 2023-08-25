public class Room
{
   //declare fields
   private String name;
   private double length;
   private double width;
   private String shadeAmount;
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
   }
   
   //constructor that accepts arguments
   public Room(String n, double l, double w, String s)
   {
      name = n;
      length = l;
      width = w;
      shadeAmount = s;
   }

   //setters
   public void setName(String n)
   {
      name = n;
   }
   
   public void setShadeAmount(String shade)
   {
      shadeAmount = shade;
   }
   
   public void setLength(double l)
   {
      length = l;
   }
   
   public void setWidth(double w)
   {
      width = w;
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
       
}