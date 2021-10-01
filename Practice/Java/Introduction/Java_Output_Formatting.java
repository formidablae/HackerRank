import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            System.out.println("================================");
            for(int i=0; i<3; i++){
                String s1 = sc.next();
                int x = sc.nextInt();
                //Complete this line
                String textX = String.valueOf(x);
                int stringlength = s1.length();
                int textXlength = textX.length();
                String spaces = "               "; //15 
                String zeros = "000";
                String column1 = s1 + (spaces.substring(0, 15 - stringlength));
                String column2 = (zeros.substring(0, 3 - textXlength)) + textX;
                System.out.printf(column1 + column2 + "\n");
            }
            System.out.println("================================");

    }
}

