package PalindromicSubstrings;

public class PalindromicSubstrings {
    public int countSubstrings(String s) {
        int count = 0;
        for(int i = 0; i < s.length() - 1; i++) {
            int oddCount = extendPalindrome(s, i, i);
            int evenCount = extendPalindrome(s, i, i + 1);
            count += oddCount + evenCount;
        }
        return count + 1; // we need to account for s.length() - 1;
    }

    public int extendPalindrome(String s, int start, int end) {
        int count = 0;
        while(start >= 0 && end < s.length()) {
            if(s.charAt(start--) == s.charAt(end++)) count++;
            else return count;
        }
        return count;
    }
}
