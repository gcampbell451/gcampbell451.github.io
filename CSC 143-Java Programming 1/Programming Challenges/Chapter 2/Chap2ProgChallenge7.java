import java.util.Scanner;

public class Chap2ProgChallenge7
{
   public static void main(String[] args)
   {
          
     final double STATE_TAX = .04;
     final double COUNTY_TAX = .02;
     double price;
     double totalState = 0;
     double totalCounty = 0;
     double totalTax = 0;
     double totalCost = 0;
     
     Scanner keyboard = new Scanner(System.in);
     
     System.out.print("How much is your purchase?");
     price = keyboard.nextDouble();
     
     totalState = price * STATE_TAX;
     totalCounty = price * COUNTY_TAX;
     totalTax = totalState + totalCounty;
     totalCost = price + totalTax;
     
     System.out.printf("Purchase Amount: $%,.2f\n\n\t State Tax: $%,.2f\n\t County Tax: $%,.2f\n\t Total Tax: $%,.2f\n\n Total Cost: $%,.2f", price, totalState, totalCounty, totalTax, totalCost);
     
     
     
   }
}