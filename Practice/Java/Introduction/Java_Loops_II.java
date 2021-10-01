import java.util.*;
import java.io.*;
import java.lang.Math;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int resultInt = 0;
            String resultString = "";
            for (int j = 0; j < n; j++) {
                if (j == 0) {
                    resultInt = a;
                }
                double resultDouble = resultInt + (java.lang.Math.pow(2, j))*b;
                resultInt = (int) resultDouble;
                resultString = String.valueOf(resultInt);
                System.out.printf(resultString);
                if (j != n-1){
                    System.out.printf(" ");
                }
                else {
                    System.out.printf("\n");
                }
            }
        }
        in.close();
    }
}

