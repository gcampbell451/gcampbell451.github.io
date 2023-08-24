import java.util.Scanner;
public class Chap4ProgChallenge11 {
   public static void main(String[] args) {
      Scanner keyboard = new Scanner(System.in);
     
     double degF = 0;
      
     System.out.println("Temp C\t\tTempF");
     for (int i = 0; i <= 20; i++) {
        degF = (9.0/5 * i) + 32;
        System.out.printf("\n%d\t\t\t\t%.2f", i, degF);
     }
     
     

      
      
         
   
      
   
   
   }
}