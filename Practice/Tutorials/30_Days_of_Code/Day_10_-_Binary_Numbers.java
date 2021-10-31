import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        boolean continueLoop = true;
        String digits = "";
        int consecutiveCount = 0;

        while(continueLoop)
        {
            digits = digits + (n % 2);
            n = n / 2;
            if (n == 0)
            {
                continueLoop = false;
            }
        }
        if(digits.length() == 0)
        {
            System.out.println(0);
        }
        else if (digits.length() == 1)
        {
            System.out.println(1);
        }
        else
        {
            String[] onlyOnesArray = digits.split("0");

            for (int i = 0; i < onlyOnesArray.length; i++)
            {
                if (onlyOnesArray[i].length() > consecutiveCount)
                {
                    consecutiveCount = onlyOnesArray[i].length();
                }
            }
        }

        System.out.println(consecutiveCount);

        scanner.close();
    }
}
