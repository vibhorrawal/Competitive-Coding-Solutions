import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
 public static void main(String[] args)
 {
     Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            long[] array = new long[2];
           
            for (int n = 0; n < 2; n++) {
                array[n] = (long) scanner.nextInt();
            }
            long val = (array[0] + array[1]) * 2;
            System.out.println(val);
        }
 }
}
