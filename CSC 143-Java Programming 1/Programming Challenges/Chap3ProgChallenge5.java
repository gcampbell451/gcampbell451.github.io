import java.util.Scanner;
public class Chap3ProgChallenge5
{
   public static void main(String[] args)
   {
      
      Scanner keyboard = new Scanner(System.in);
      
      final double GRAVITY = 9.8;
      double mass = 0;
      double weight = 0;
      
    
      
      System.out.print("Enter the object's mass in kg: ");
      mass = keyboard.nextDouble();
          
      weight = mass * GRAVITY;
      
    
      if (weight > 1000)
         System.out.printf("The object weighs %,.2f Newtons and is too heavy.", weight);
      else if (weight < 10)
         System.out.printf("The object weighs %.2f Newtons and is too light.", weight);
      else
         System.out.printf("The object weighs %.2f Newtons and is just right.", weight);
      
      
   }
}