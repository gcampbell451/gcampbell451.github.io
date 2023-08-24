import java.util.Scanner;
public class Chap3ProgChallenge3
{
   public static void main(String[] args)
   {
      
      Scanner keyboard = new Scanner(System.in);
      
      double weight = 0;
      double height = 0;
      double bmi = 0;
    
      
      System.out.print("Enter your weight in pounds: ");
      weight = keyboard.nextDouble();
      
      System.out.print("Enter your height in inches: ");
      height = keyboard.nextDouble();
      
      bmi = weight * (703 / Math.pow(height, 2.0);
      
    
      if (bmi < 18.5)
         System.out.printf("Your BMI is %.2f and you are underweight.", bmi);
      else if (bmi < 25)
         System.out.printf("Your BMI is %.2f and your weight is optimal", bmi);
      else
         System.out.printf("Your BMI is %.2f and you are a fatty.", bmi);
      
      
   }
}