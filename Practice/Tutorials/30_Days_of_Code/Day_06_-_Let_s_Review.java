import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args)
    {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int numberOfInputsLines = Integer.parseInt(input.nextLine());

        for (int i = 0; i < numberOfInputsLines; i++)
        {
            String lineText = input.nextLine();
            
            String[] lineTextArray = lineText.split("");
            for (int j = 0; j < lineTextArray.length; j = j + 2)
            {
                System.out.print(lineTextArray[j]);
            }

            System.out.print(" ");

            for (int j = 1; j < lineTextArray.length; j = j + 2)
            {
                System.out.print(lineTextArray[j]);
            }

            System.out.println();
        }
    }
}
