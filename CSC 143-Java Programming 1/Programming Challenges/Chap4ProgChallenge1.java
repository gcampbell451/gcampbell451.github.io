import java.util.Scanner;
public class Chap4ProgChallenge1 {
   public static void main(String[] args) {
      Scanner keyboard = new Scanner(System.in);
      
     int num = 0;
     int total = 0;
     
     System.out.print("Enter a nonzero integer: ");
     num = keyboard.nextInt();
     
     for (int i = 1; i <= num; i++){
         total += i;
         System.out.println(total);
     }
      
      
      
         
   
      
   
   
   }
}