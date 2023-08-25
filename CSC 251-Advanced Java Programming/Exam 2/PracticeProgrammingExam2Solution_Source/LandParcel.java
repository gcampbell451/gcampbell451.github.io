public class LandParcel
{
   private int parcelID;
   private double size;
   private String zoning;
   private Building building;//this is the aggregation ("has a" relationship) - because the LandParcel "has a" Building object as a field
   
   /**
   no-arg constructor
   */
   public LandParcel()
   {
      parcelID = 0;
      size = 0;
      zoning = "";
      building = new Building();
   }
   
   /**
   A Constructor for the LandParcel class
   @param parcelID the parcel's ID number
   @param size the size of the parcel (in acres)
   @param zoning the zoning type (Commercial or Residential)
   @param b the Building located on this LandParcel
   */
   public LandParcel(int parcelID, double size, String zoning, Building building)
   {
      this.parcelID = parcelID;
      this.size = size;
      this.zoning = zoning;
      //this.building = building;//this is a shallow copy, which we do NOT want to do
      this.building = new Building(building);//we use the copy constructor here to avoid a security hole by making a reference directly to the parameter "b" that we were passed
      
   }
   
   /**
   @return the parcel's ID number
   */
   public int getParcelID()
   {
      return parcelID;
   }
   
   /**
   @return the parcel's size (in acres)
   */
   public double getSize()
   {
      return size;
   }
   
   /**
   @return the zoning type (Residential or Commercial)
   */ 
   public String getZoning()
   {
      return zoning;
   }
   
   /**
   @return the Building located on this LandParcel
   */
   public Building getBuilding()
   {
      //return building;//this returns a reference to our internal Building object, which we want to avoid
      return new Building(building);//we use the copy constructor here to avoid a security hole by returning a direct reference to our Building field "b"
   }
   
   /**
   @param parcelID the parcel's ID number
   */
   public void setParcelID(int parcelID)
   {
      this.parcelID = parcelID;
   }
   
   /**
   @param size the parcel's size (in acres)
   */
   public void setSize(double size)
   {
      this.size = size;
   }
   
   /**
   @param zoning the zoning type (Residential or Commercial) 
   */
   public void setZoning(String zoning)
   {
      this.zoning = zoning;
   }
   
   /**
   @param b the Building located on this LandParcel
   */
   public void setBuilding(Building building)
   {
      //this.building = building; //this is a shallow copy, which we do NOT want to do
      this.building = new Building(building);//we use the copy constructor here to avoid a security hole by making a reference directly to the parameter "b" that we were passed
   }
   
   /**
   Calculates the property tax for this LandParcel
   @return the property tax
   */
   public double getPropertyTax()
   {
      final double BASE_AMOUNT_RESIDENTIAL = 500;
      final double BASE_AMOUNT_COMMERCIAL = 2000;
      final double ADDITIONAL_COST_RESIDENTIAL_SMALL = 0.50;
      final double ADDITIONAL_COST_RESIDENTIAL_LARGE = 0.75;
      final double ADDITIONAL_COST_COMMERCIAL_SMALL = 1.00;
      final double ADDITIONAL_COST_COMMERCIAL_LARGE = 1.50;
      final double SIZE_CUTOFF_RESIDENTIAL = 2000;
      final double SIZE_CUTOFF_COMMERCIAL = 4000;
      
      double baseAmount = 0;
      double buildingCostPerSqFt = 0;
      
      if(zoning.equalsIgnoreCase("Commercial"))
      {
         baseAmount = BASE_AMOUNT_COMMERCIAL;//base amount of 2000 per acre
         if(building.getSize() < SIZE_CUTOFF_COMMERCIAL)
         {
            buildingCostPerSqFt = ADDITIONAL_COST_COMMERCIAL_SMALL;//additional $1 per square foot on top of the base amount
         }
         else
         {
            buildingCostPerSqFt = ADDITIONAL_COST_COMMERCIAL_LARGE;//additional $1.50 per square foot on top of the base amount
         }
      }
      else//residential
      {
         baseAmount = BASE_AMOUNT_RESIDENTIAL;//base amount of 500 per acre
         if(building.getSize() < SIZE_CUTOFF_RESIDENTIAL)
         {
           buildingCostPerSqFt = ADDITIONAL_COST_RESIDENTIAL_SMALL;//additional $0.50 per square foot on top of the base amount
         }
         else
         {
            buildingCostPerSqFt = ADDITIONAL_COST_RESIDENTIAL_LARGE;//additional $0.75 per square foot on top of the base amount
         }
      }
      
      return (size * baseAmount) + (building.getSize() * buildingCostPerSqFt);
   }
   
   /**
   @return a String representation of the LandParcel
   */
   public String toString()
   {
      return String.format("Parcel ID: " + parcelID +
             "\nParcel Size: " + size + " acres" +
             "\nParcel Zoning: " + zoning +
             "\n" + building + //implicitly call the Building class' toString method here
             "\nProperty Tax: $%,.2f", getPropertyTax());
   }
   
}