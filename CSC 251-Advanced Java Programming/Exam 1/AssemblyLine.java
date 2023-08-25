public class AssemblyLine
{
   // instance fields
   private String name;
   private double widgetsMade;
   private double rejectedWidgets;
   
   // no-arg constructor
   public AssemblyLine()
   {
      name = "no name";
      widgetsMade = 0;
      rejectedWidgets = 0;
   }
   
   // constructor that passes arguments to all fields
   public AssemblyLine(String n, double w, double r)
   {
      name = n;
      widgetsMade = w;
      rejectedWidgets = r;
   }
   
   // mutators
   public void setName(String n)
   {
      name = n;
   }
   
   public void setWidgetsMade(double w)
   {
      widgetsMade = w;
   }
   
   public void setRejectedWidgets(double r)
   {
      rejectedWidgets = r;
   }
   
   // accessors
   public String getName()
   {
      return name;
   }
   
   public double getWidgetsMade()
   {
      return widgetsMade;
   }
   
   public double getRejectedWidgets()
   {
      return rejectedWidgets;
   }
   
   // methods 
   // calculate based on given formulae
   public double calcAcceptableWidgets()
   {
      return widgetsMade - rejectedWidgets;
   }
   
   public double calcAssemblyLineQuality()
   {
      return (calcAcceptableWidgets() / widgetsMade) * 100;
   }
   
}