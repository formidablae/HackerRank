import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        /* Enter your code here. Print output to STDOUT. */
        boolean isPalindrome = true;
        String substrLeft = "";
        String substrRight = "";
        for (int i = 0; i < (A.length() / 2); i++) {
            substrLeft = A.substring(i, i + 1);
            substrRight = A.substring((A.length() - i - 1), (A.length() - i));
            if (!(substrLeft.compareTo(substrRight) == 0)) {
                isPalindrome = false;
                i = (A.length() / 2);
            }
        }
        if (isPalindrome) System.out.println("Yes");
        else System.out.println("No");
    }
}

