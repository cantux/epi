package PermuationInString;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/**
 * Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
 * In other words, one of the first string's permutations is the substring of the second string.
 */
public class PermutationInString {
    public static void main(String[] args) {
        System.out.println("result: " + checkInclusion("ab", "eidbaooo"));
        System.out.println("result: " + checkInclusion("ab", "eidboaoo"));
    }

    public static boolean checkInclusion(String s1, String s2) {
        return checkInclusionHelper(s1, s2, false);
    }

    public static boolean checkInclusionHelper(String s1, String s2, boolean foundPermutation) {
        if(s2.length() < s1.length()) {
            return false;
        }
        if(s1.length() <= s2.length()) {
            foundPermutation = permutationTester(s1, s2.substring(0, s1.length()));
        }
        return foundPermutation || checkInclusion(s1, s2.substring(1));
    }

    public static boolean permutationTester(String s1, String s2) {
        Map<Character, Integer> letterMap = new HashMap<Character, Integer>();
        // we are sure at this function that given
        for(int i = 0; i < s2.length(); i++) {
            if(letterMap.containsKey(s2.charAt(i))) {
                int count = letterMap.get(s2.charAt(i));
                letterMap.put(s2.charAt(i), ++count);
            }
            else {
                letterMap.put(s2.charAt(i), 1);
            }
        }

        for(int i = 0; i < s2.length(); i++) {
            char c = s1.charAt(i);
            if(letterMap.containsKey(c)) {
                int count = letterMap.get(c);
                letterMap.put(c, --count);
            }
            else {
                return false;
            }
        }

        Set<Map.Entry<Character, Integer>> entSet = letterMap.entrySet();
        Iterator<Map.Entry<Character,Integer>> it = entSet.iterator();

        while(it.hasNext()) {
            Map.Entry<Character,Integer> entry = it.next();
            if(entry.getValue() != 0) {
                return false;
            }
        }

        return true;
    }
}
