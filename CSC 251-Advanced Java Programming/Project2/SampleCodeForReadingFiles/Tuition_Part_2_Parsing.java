import java.util.*; 
import java.io.*;

public class Tuition_Part_2_Parsing 

{ //open the class container


   public static void main(String[] args)
   { //open the main method                              
      
             
        /*The book uses the "throws IOException" option in the main method header. In this exercise we use a "try" and "catch" process. We "try" to open the file and process it, but if something goes wrong, 
        an IOException will be "thrown" and we can "catch" it and deal with the problem. By taking this approach instead of adding a "throws IOException" clause to the main method header, we can 
        gracefully handle problems related to reading the file without having our program crash. If a problem occurs while processing the file, the IOException is immediately "thrown", the code 
        immediately jumps to the "catch" block of code. The message in the "catch" block will display. */

      try 
      {
         /*Create an instance of the File class. Pass the string "tuition.txt" to the constructor. 
         This process creates a File object that represents the file tuition.txt.*/
         File file = new File("tuition.txt");
          
         /* Pass a reference to the File object as an argument to the Scanner class constructor (i.e., file) */                             
         Scanner inputFile = new Scanner(file);
      
         //declare the variables
         String courseNumber = "", courseName = "", fileInput = " ";
         double contactHours = 0.0, creditHours = 0.0, totalTuitionCost = 0.0;
      
         //Create an array list to store objects. The ArrayList will hold Course objects.
         ArrayList<Course> courses = new ArrayList<Course>();
      
         /* Use a while loop to read the file. Use the hasNext() method to determine whether 
            the file has more data to be read. Use an "if statement" to determine the end of the file and 
            to consume newline characters */
      
         while(inputFile.hasNext())       
         { //open loop
         
            courseNumber = inputFile.nextLine();//read the next line of the file as a String and assign the input to the courseNumber variable
            
            courseName = inputFile.nextLine();//read the next line of the file as a String and assign the input to the courseNumber variable
            
            fileInput = inputFile.nextLine();//read the next line of the file as a String
            contactHours = Double.parseDouble(fileInput);//convert the input into a double and assign to the contactHours variable
            
            fileInput = inputFile.nextLine();//read the next line of the file as a String
            creditHours = Double.parseDouble(fileInput);//convert the input into a double and assign to the creditHours variable
         
            if(inputFile.hasNext())
            { 
               inputFile.nextLine();//skip the blank line if we have not reached the end of the file
            }
         
            /* Create Course objects using the Course class type - we are still under the while loop. Objects will be created as long as there are records
            in the file to read.*/
            Course c = new Course(courseNumber, courseName, contactHours ,creditHours); //Passing variables as arguments to the constructor
         
            /* Add Course objects to the ArrayList (Note: courses is the reference variable for the ArrayList and c is the
            reference variable for the Course objects)*/
            courses.add(c); 
         
         } //close loop
      
         inputFile.close();//close the file 
               
         //use a for loop to display the output
         for(int i =0; i < courses.size(); i++)
         { 
            System.out.println( "Course Name: " + courses.get(i).getCourseName()); //instance method - returns the course name
            System.out.println( "Course Number: " + courses.get(i).getCourseNumber()); //instance method - returns the course number
            System.out.println( "Contact Hours: " + courses.get(i).getContactHours()); //instance method - returns the contact hours
            System.out.println( "Credit Hours: " + courses.get(i).getCreditHours()); //instance method - returns the credit hours
            System.out.printf( "Tuition Cost: $%.2f \n", courses.get(i).getTuitionCost()); //method that returns the tuition for each course
            System.out.println();
         
            totalTuitionCost += courses.get(i).getTuitionCost();//add the tution cost of the current course to our accumulator 
         }  
           
         System.out.printf("Total Tuition Cost: $%,.2f \n", totalTuitionCost); //print out the total tuition cost
      
      }//close the "try" block of code
      
      catch(IOException ex)//If something goes wrong, an IOException is "thrown" to us, and we "catch" it and deal with it
      {
         //use the getMessage method of the exception we "caught" to print out it's message about what went wrong
         System.out.println("Something went wrong reading the file: " + ex.getMessage());
      }
      
   } //close main
   
} //close the class container