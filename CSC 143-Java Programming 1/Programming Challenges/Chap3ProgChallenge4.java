import java.util.Scanner;
public class Chap3ProgChallenge4
{
   public static void main(String[] args)
   {
      
      Scanner keyboard = new Scanner(System.in);
      
      double score1 = 0;
      double score2 = 0;
      double score3 = 0;
      double averageScore = 0;
      String grade = "";
    
      
      System.out.print("Enter your first test score: ");
      score1 = keyboard.nextDouble();
      
      System.out.print("Enter your second test score: ");
      score2 = keyboard.nextDouble();
      
      System.out.print("Enter your third test score: ");
      score3 = keyboard.nextDouble();
      
      averageScore = (score1 + score2 + score3)/3;
      
    
      if (averageScore < 60)
      {  
         grade = "F";
         System.out.printf("Your score average is %.02f and your grade is a %s.", averageScore, grade);
      }
      else if (averageScore < 70)
      {
         grade = "D";
         System.out.printf("Your score average is %.02f and your grade is a %s.", averageScore, grade);
      }
      else if (averageScore < 80)
      {
         grade = "C";
         System.out.printf("Your score average is %.02f and your grade is a %s.", averageScore, grade);
      }
      else if (averageScore < 90)
      {
         grade = "B";
         System.out.printf("Your score average is %.02f and your grade is a %s.", averageScore, grade);
      }
      else if (averageScore < 100)
      {
         grade = "A";
         System.out.printf("Your score average is %.02f and your grade is an %s.", averageScore, grade);
      }
      else
            System.out.printf("You achieved a perfect score of 100 and your grade is an A!");
      
      
   }
}