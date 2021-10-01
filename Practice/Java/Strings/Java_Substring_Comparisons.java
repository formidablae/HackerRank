public static String getSmallestAndLargest(String s, int k) {
    String smallest = "";
    String largest = "";
    
    // Complete the function
    // 'smallest' must be the lexicographically smallest substring of length 'k'
    // 'largest' must be the lexicographically largest substring of length 'k'
    for (int i = 0; i <= (s.length() - k); i++) {
        String substr = s.substring(i, i + k);
        if (smallest.equals("")) {
            smallest = substr;
        } else {
            if (smallest.compareTo(substr) > 0) {
                smallest = substr;
            }
        }
        if (largest.equals("")) {
            largest = substr;
        } else {
            if (largest.compareTo(substr) < 0) {
                largest = substr;
            }
        }
    }
    
    return smallest + "\n" + largest;
}

