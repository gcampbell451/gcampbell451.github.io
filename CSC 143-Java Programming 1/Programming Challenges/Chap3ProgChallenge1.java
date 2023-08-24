import java.util.Scanner;

public class Chap3ProgChallenge1
{
   public static void main(String[] args)
   {
          
     int userNum = 0;
     String romanNum = "";
     
     Scanner keyboard = new Scanner(System.in);
     
     System.out.print("Enter a number between 1 and 10: ");
     userNum = keyboard.nextInt();
     
     
     switch (userNum)
     {
         case 1:
            romanNum = "I";
            break;
         case 2:
            romanNum = "II";
            break;
         case 3:
            romanNum = "III";
            break;
         case 4:
            romanNum = "IV";
            break;
         case 5:
            romanNum = "V";
            break;
         case 6:
            romanNum = "VI";
            break;
         case 7:
            romanNum = "VII";
            break;
         case 8:
            romanNum = "VIII";
            break;
         case 9:
            romanNum = "IX";
            break;
         case 10:
            romanNum = "X";
            break;
         default:
            romanNum = "You did not enter a number between 1 and 10. Please try again.";             
     }
     
         System.out.printf("That number translated to Roman numerals is %s.", romanNum); 
     
     
   }
}