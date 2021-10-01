static boolean isAnagram(String a, String b) {
    // Complete the function

    a = a.toUpperCase();
    b = b.toUpperCase();

    if (a.length() != b.length()) {
        return false;
    } else if (a.equals(b)) {
        return true;
    } else {
        for(int i = 0; i <= (a.length() - 2); i++) {
            if((a.substring(i, (i + 1))).compareTo(a.substring((i + 1), (i + 2))) > 0) {
                if(i == 0 && a.length() > 2) {
                    a = a.substring((i + 1), (i + 2)) + a.substring(i, (i + 1)) + a.substring(i + 2, a.length());
                } else if(i == 0 && a.length() == 2) {
                    a = a.substring((i + 1), (i + 2)) + a.substring(i, (i + 1));
                } else if(i == (a.length() - 2)) {
                    a = a.substring(0, i) + a.substring((i + 1), (i + 2)) + a.substring(i, (i + 1));
                } else {
                    a = a.substring(0, i) + a.substring((i + 1), (i + 2)) + a.substring(i, (i + 1)) + a.substring(i + 2, a.length());
                }
                i = -1;
            }
        }

        for(int i = 0; i <= (b.length() - 2); i++) {
            if((b.substring(i, (i + 1))).compareTo(b.substring((i + 1), (i + 2))) > 0) {
                if(i == 0 && b.length() > 2) {
                    b = b.substring((i + 1), (i + 2)) + b.substring(i, (i + 1)) + b.substring(i + 2, b.length());
                } else if(i == 0 && b.length() == 2) {
                    b = b.substring((i + 1), (i + 2)) + b.substring(i, (i + 1));
                } else if(i == (b.length() - 2)) {
                    b = b.substring(0, i) + b.substring((i + 1), (i + 2)) + b.substring(i, (i + 1));
                } else {
                    b = b.substring(0, i) + b.substring((i + 1), (i + 2)) + b.substring(i, (i + 1)) + b.substring(i + 2, b.length());
                }
                i = -1;
            }
        }
        return a.equals(b);
    }
}

