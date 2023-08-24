import java.util.Scanner;

public class Chap2ProgChallenge10
{
   public static void main(String[] args)
   {
          
     String favCity = "";
     
     Scanner keyboard = new Scanner(System.in);
     
     System.out.print("What is your favorite city? ");
     favCity = keyboard.nextLine();
     
     System.out.println(favCity.length());
     System.out.println(favCity.toUpperCase());
     System.out.println(favCity.toLowerCase());
     System.out.println(favCity.charAt(0));
     
     
     
     
   }
}