package isUnique;

import java.util.HashSet;

public class IsUnique {

    public static void main(String[] args) {
        String[] test = {
                "asdf",
                "aaaa",
                "asdff"
        };

        for (String a : test) {
            System.out.println("Result for N^2 a: " + a + " is: " + checkUniqueN2(a));
        }
        for (String a : test) {
            System.out.println("Result for N a: " + a + " is: " + checkUniqueN(a));
        }
    }

    public static boolean checkUniqueN2(String s) {
        for (int i = 0 ; i < s.length(); i++) {
            char currChar = s.charAt(i);
            for (int j = 0; j < s.length(); j++) {
                if(i != j && currChar == s.charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean checkUniqueN(String s) {
        HashSet hs = new HashSet();
        for(int i = 0; i < s.length(); i++) {
            if(hs.contains(s.charAt(i))) {
                return false;
            }
            hs.add(s.charAt(i));
        }
        return true;
    }

}