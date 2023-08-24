public class Chap2ProgChallenge5
{
   public static void main(String[] args)
   {
     final double TOTAL_SALES = 4600000;
     final double PERCENT_SALES = .62;
     double eastCoastSales = 0;
     
     eastCoastSales = TOTAL_SALES * PERCENT_SALES;
     System.out.printf("If total sales are %,.0f then the East Coast sales division will generate %,.0f in sales.", TOTAL_SALES, eastCoastSales);
     
     
     
   }
}