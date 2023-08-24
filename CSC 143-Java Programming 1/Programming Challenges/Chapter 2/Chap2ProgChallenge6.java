public class Chap2ProgChallenge6
{
   public static void main(String[] args)
   {
     final double ONE_ACRE = 43560;
     double myLand = 389767;
     double myAcres = myLand / ONE_ACRE;
     
     System.out.printf("I have %,.0f square feet of land so\n I have %.2f acres.", myLand, myAcres);
     
     
   }
}