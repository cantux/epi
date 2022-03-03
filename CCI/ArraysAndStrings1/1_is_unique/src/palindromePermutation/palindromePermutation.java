package palindromePermutation;

import java.util.HashSet;

public class palindromePermutation {
    public static void main (String [] args) {
        String[] test = {
                "a",
                "bb",
                "bba",
                "aaaa",
                "asdff"
        };

        for (String a : test) {
            System.out.println("Result for N^2 a: " + a + " is: " + checkPalinPerm(a));
        }
    }
    public static boolean checkPalinPerm(String str) {
        HashSet<Character> hs = new HashSet<>();
        for(int i = 0; i < str.length(); i++) {
            char currentChar = str.charAt(i);
            if(hs.contains(currentChar))
            {
                hs.remove(currentChar);
            }
            else
            {
                hs.add(currentChar);
            }
        }

        return hs.size() < 2;
    }

}
