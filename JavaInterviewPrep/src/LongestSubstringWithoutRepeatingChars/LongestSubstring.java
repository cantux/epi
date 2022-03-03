package LongestSubstringWithoutRepeatingChars;

import java.util.HashSet;
import java.util.Set;

public class LongestSubstring {



    // sliding window
    public int lengthOfLongestSubstring1(String s) {
        int length = s.length();
        Set<Character> set = new HashSet<>();
        int max = 0, start = 0, end = 0;
        while(start < length && end < length) {
            if(!set.contains(s.charAt(end))) {
                set.add(s.charAt(end));
                end++;
                max = Math.max(max, end - start);
            }
            else {
                set.remove(s.charAt(start));
                start++;
            }
        }
        return max;
    }

    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0) return 0;

        Set<Character> tempCharSet = new HashSet();

        int startOfLongest = 0, endOfLongest = 0, maxLength = Integer.MIN_VALUE, currentLength = 0;
        for(int i = 0; i < s.length(); i++) {
            for(int j = i; j < s.length(); j++) {
                char c = s.charAt(j);
                if(tempCharSet.contains(c)) {
                    maxLength = Math.max(maxLength, tempCharSet.size());
                    tempCharSet = new HashSet();
                    tempCharSet.add(c);
                }
                else {
                    currentLength++;
                    tempCharSet.add(c);
                }
            }
            maxLength = Math.max(maxLength, tempCharSet.size());
            tempCharSet = new HashSet();
        }


        return maxLength;
    }
}
