
import java.util.*;


public class Main {

   public static void test()
   {

   }
   public static void main(String[] args) {
      int ii = 0;

      switch(ii)
      {
         case 0:
            test();
            break;
         case 1:
            return;
         default:
            System.exit(0);
      }

      while(ii < 5)
      {
         ii++;
         break;
         System.out.println("ok");
         return;
      }

      return;
   }

}