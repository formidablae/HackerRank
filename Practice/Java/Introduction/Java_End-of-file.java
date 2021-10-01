import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */                           InputStream is = null;
        BufferedReader br = null;
        int i = 1;
        try {
            is = System.in;
            br = new BufferedReader(new InputStreamReader(is));
            String line = null;
            while ((line = br.readLine()) != null) {
                if (line.equalsIgnoreCase("quit")) {
                    break;
                }
                System.out.println(i + " " + line);
                i++;
            }
        }
        catch (IOException ioe) {
            System.out.println("Exception while reading input " + ioe);
        }
        finally {
            // close the streams using close method
            try {
                if (br != null) {
                    br.close();
                }
            }
            catch (IOException ioe) {
                System.out.println("Error while closing stream: " + ioe);
            }
        }
    }
}

