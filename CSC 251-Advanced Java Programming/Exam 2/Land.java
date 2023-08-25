public class Land
{
   // instance fields
   private String parcelId, zoningType;
   private double acreage;
   private Building building;
   
   // no-arg constructor
   public Land()
   {
      parcelId = "";
      acreage = 0.0;
      zoningType = "";
      building = new Building();
   }
   
   // constructor that accepts args
   public Land(String parcelId, double acreage, String zoningType, Building building)
   {
      this.parcelId = parcelId;
      this.acreage = acreage;
      this.zoningType = zoningType;
      this.building = new Building(building);
   }
   
   // copy constructor
   public Land(Land obj2)
   {
      parcelId = obj2.parcelId;
      acreage = obj2.acreage;
      zoningType = obj2.zoningType;
      building = new Building(obj2.getBuilding());
   }
   
   // mutators
   public void setParcelId(String parcelId)
   {
      this.parcelId = parcelId;
   }
   
   public void setAcreage(double acreage)
   {
      this.acreage = acreage;
   }
   
   public void setZoningType(String zoningType)
   {
      this.zoningType = zoningType;
   }
   
   public void setBuilding(Building building)
   {
      this.building = new Building(building);
   }
   
   // accessors
   public String getParcelId()
   {
      return parcelId;
   }
   
   public double getAcreage()
   {
      return acreage;
   }
   
   public String getZoningType()
   {
      return zoningType;
   }
   
   public Building getBuilding()
   {
      return new Building(building);
   }
   
  public double calcTax()
    {
      // initialize local variable to store and return tax
      double propTax = 0.0;
     
      // constants
      final double COMMERCIAL_SMALL_COST = 1.00;
      final double COMMERCIAL_LARGE_COST = 1.50;
      final double RESIDENTIAL_SMALL_COST = 0.50;
      final double RESIDENTIAL_LARGE_COST = 0.75;
      final double COMMERCIAL_BASE_COST = 2000.00;
      final double RESIDENTIAL_BASE_COST = 500.00;
     
      if (zoningType.equalsIgnoreCase("commercial"))
      {
         if (building.getSqFootage() < 4000)
            propTax = (acreage * COMMERCIAL_BASE_COST) + (building.getSqFootage() * COMMERCIAL_SMALL_COST);
         else
            propTax = (acreage * COMMERCIAL_BASE_COST) + (building.getSqFootage() * COMMERCIAL_LARGE_COST);
      }
      else
         {
         if (building.getSqFootage() < 2000)
            propTax = (acreage * RESIDENTIAL_BASE_COST) + (building.getSqFootage() * RESIDENTIAL_SMALL_COST);
         else
            propTax = (acreage * RESIDENTIAL_BASE_COST) + (building.getSqFootage() * RESIDENTIAL_LARGE_COST);
      }
      return propTax;
   }
   
   // toString
   public String toString()
   {
      return String.format("Parcel Id: " + parcelId + 
                           "\nAcreage: %,.2f" + 
                           "\nZoning Type: " + zoningType + 
                           "\nBuilding Information: \n" + building, acreage);
   }
      
   
}