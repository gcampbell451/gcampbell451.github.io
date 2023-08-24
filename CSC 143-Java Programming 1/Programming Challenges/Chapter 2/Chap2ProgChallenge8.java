import java.util.Scanner;

public class Chap2ProgChallenge8
{
   public static void main(String[] args)
   {
          
     final double TOTAL_COOKIES = 40;
     final double CALORIES_IN_SERVING = 300;
     final double SERVINGS_IN_BAG = 10;
     int numCookies = 0;
     double numServings = 0;
     double totalCalories = 0;
     
     Scanner keyboard = new Scanner(System.in);
     
     System.out.print("How many cookies did you eat? ");
     numCookies = keyboard.nextInt();
     
     numServings = numCookies * (SERVINGS_IN_BAG / TOTAL_COOKIES);
     totalCalories = numServings * CALORIES_IN_SERVING;
     
     System.out.printf("\n\nYou consumed %,.0f calories.", totalCalories);     
     
     
     
     
   }
}