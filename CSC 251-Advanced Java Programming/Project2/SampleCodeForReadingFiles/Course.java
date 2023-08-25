/* First step: 
Create the class. Once the class is created, we can use the class to create 
objects in the demo program.*/

public class Course
//open the class
{

   //fields 
   /* We use the private access modifier because the class is "hiding" its data from outside code.
   The use of the private access modifier protects data from corruption. 
   
   When an object is created in the program, the object will
   have it's own "instance" fields: courseNumber, courseName, contactHours, creditHours.*/
   
   private String courseNumber, courseName; 
   private double contactHours, creditHours;
   private final double COST_PER_HR = 72; 
   
   
   
   /*The constructor has the same name as the class.
   The constructor will be used to "construct" or "create" an object in the demo program. It will be used to "store" 
   initial values in the object's instance fields */
     
   public Course( String cNum, String cName, double contHrs, double credHrs)
   {
   
   /*An object will be created by calling the constructor in the demo program. 
     The constructor in the demo program will accept 4 arguments. These arguments will be passed to the four 
     parameter variables (parameter variables in this example: cNum, cName, contHrs, credHrs). The parameter variables are assigned
     to the "instance" fields that belong to the object. */
     
      courseNumber = cNum;
      courseName = cName;
      contactHours = contHrs;
      creditHours = credHrs;
   }
   
   
   //Setter methods 
      
   /*When an object is created in the demo program, the object will
   have it's own "instance" methods: setCourseNumber, setCourseName, setContactHours, setCreditHours)*/

   /*The setter methods are "void." We are not returning data to a statement that may call the method in the demo program.
   The set methods have a parameter variable (i.e., String cNum, for example is the parameter variable for the
   setCourseNumber method. If the course number changes in the program, the setCourseNumber method can be called to 
   change the course number.*/
         
   /* We can use the set methods in the demo program to "change" a value in an instance field.*/
   
   /* Please note: If a no arg constructor is added to this class, you can call a no-arg constructor in the demo program 
   and use the "set" methods to store a value in an instance field. In this class, we do not have a 
   no-arg constructor, our constructor accepts arguments. */

      
   public void setCourseNumber(String cNum)
   {
      courseNumber = cNum;
   }

   public void setCourseName(String cName)
   {
      courseName = cName;
   }

   public void setContactHours(double cHours)
   {
      contactHours = cHours;
   }

   public void setCreditHours(double cHours)
   {
      creditHours = cHours;
   }

   //Getters
   /* Our instance fields will be private; therefore, we must have getter methods to "get" the values 
   stored in an object's fields. We must include a "return" statement so the value is returned
   without generating an error.*/
   
   /*When an object is created in the program, the object will
   have it's own "instance" methods: getCourseNumber, getCourseName, getContactHours, getCreditHours*/

   public String getCourseNumber()
   {
      return courseNumber;
   }

   public String getCourseName()
   {
      return courseName;
   }
   
      
   public double getContactHours()
   {
      return contactHours;
   }
   
   public double getCreditHours()
   {
      return creditHours;
   }

   /* Perform the calculation to determine the tuition
   Notice that COST_PER_HR was declared at the top of the class. It can be used by the getTuitionCost method because
   fields are "global" in a class. 

   Please note: COST_PER_HR could have been declared as a "local" variable within the getTuitionCost method. This is acceptable
   because we are using COST_PER_HR only to calculate the tuition cost. 

   We want to avoid having "stale data" by not assigning the tuition cost to a field in the method. We use only a return 
   statement to return the result of the calculation.*/
     
   public double getTuitionCost()
   {
      return creditHours * COST_PER_HR;
   }
   
   
      
//close the class     
} 