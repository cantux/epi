package FindAllAnagrams;

import java.util.ArrayList;
import java.util.List;

/**
 * Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
 */
public class FindAllAnagramsInString {
    public static void main(String[] args) {
//        System.out.println("result: " + new FindAllAnagramsInString().findAnagrams());
    }

    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> soln = new ArrayList<Integer>();
        if (s.length() == 0 || p.length() == 0 || s.length() < p.length()){
            return new ArrayList<Integer>();
        }

        // create the map
        int[] chars = new int[26];
        for (Character c : p.toCharArray()){
            chars[c-'a']++;
        }

        // keep two pointers to the start and end of the
        int start = 0, end = 0, len = p.length(), diff = len;
        char temp;
        for (end = 0; end < len; end++){
            temp = s.charAt(end);
            chars[temp-'a']--;

            if (chars[temp-'a'] >= 0){
                diff--;
            }
        }

        //This would mean that s began with an anagram of p
        if (diff == 0){
            soln.add(0);
        }

        while (end < s.length()){
            temp = s.charAt(start);
            if (chars[temp-'a'] >= 0){
                diff++;
            }

            chars[temp-'a']++;

            start++;

            temp = s.charAt(end);

            chars[temp-'a']--;

            if (chars[temp-'a'] >= 0){
                diff--;
            }

            if (diff == 0){
                soln.add(start);
            }

            end++;

        }

        return soln;


    }
}
