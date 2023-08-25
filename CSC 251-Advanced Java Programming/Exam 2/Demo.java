import java.util.Scanner;
import java.util.ArrayList;
public class Demo
{
   public static void main(String[] args)
   {
      // initialize variables for user input
      String first = "";
      String last = "";
      int idNum = 0;
      String contact = "";
      String vaxxed = "";
      String symptoms = "";
      
      // initialize variables to convert user input to boolean
      boolean userContact = true;
      boolean userVaxxed = false;
      boolean userSymptoms = true;
      
      // initialize variable to store number of forms submitted
      int formCount = 0;
      
      // initialize variable to store number of students not allowed to return to campus
      double notAllowedToReturn = 0.0;
      
      // initialize variable to store average of students allowed to return
      double average = 0.0;
      
      // initialize variable to keep program running
      String keepGoing = "Y";
      
      // create scanner object
      Scanner keyboard = new Scanner(System.in); 
      
      // create ArrayList to hold Student objects
      ArrayList<Student> demoList = new ArrayList<Student>();
      
      // begin program loop
      do
      {
         // prompt for user input to fully initialize objects
         System.out.print("What is the student's first name? ");
         first = keyboard.nextLine();
         
         System.out.print("What is the student's last name? ");
         last = keyboard.nextLine();
         
         System.out.print("What is the student's student ID number? ");
         idNum = keyboard.nextInt();
         keyboard.nextLine();
             
         System.out.print("Has the student come in contact in the past 14 day with someone believed to have contracted COVID-19 (Y/N)? ");
         contact = keyboard.nextLine();
         
         System.out.print("Has the student received a COVID-19 vaccination (Y/N)? ");
         vaxxed = keyboard.nextLine();
         
         System.out.print("Has the student had any COVID-19 symptoms in the 14-days prior to returning to campus (Y/N)? ");
         symptoms = keyboard.nextLine();
         
         // convert health form input to boolean to pass to constructor
         if (contact.equalsIgnoreCase("N"))
            userContact = false;
         else
            userContact = true;
            
         if (vaxxed.equalsIgnoreCase("Y"))
            userVaxxed = true;
         else 
            userVaxxed = false;
            
         if (symptoms.equalsIgnoreCase("N"))
            userSymptoms = false;
         else
            userSymptoms = true;         
            
         // create HealthAcknowledgementForm object
         HealthAcknowledgementForm demoForm = new HealthAcknowledgementForm(userContact, userVaxxed, userSymptoms);
         
         // create Student object
         Student demoStudent = new Student(first, last, idNum, demoForm);
         
         // increment notAllowedToReturn
         if (userSymptoms || (!userVaxxed && userContact))
            notAllowedToReturn++;
         
         // add student object to ArrayList
         demoList.add(demoStudent); 
      
         // ask user to continue or quit   
         System.out.print("Do you wish to enter information for another student (Y/N)? ");
         keepGoing = keyboard.nextLine();
         
      } while (keepGoing.equalsIgnoreCase("Y"));
      
      // display header
      System.out.println("Return to Campus Student Tracking System");
      
      // display info
      for (int i = 0; i < demoList.size(); i++)
         System.out.print(demoList.get(i));    
      
      formCount = HealthAcknowledgementForm.getTotalForms();
     
      average = notAllowedToReturn / formCount * 100;
      System.out.println("\n\nTotal number of Health Acknowledgement Forms: " + formCount);
      System.out.printf("\nPercentage of students not allowed to return to campus: %.2f", average);
      
   }// end of main
}// end of class