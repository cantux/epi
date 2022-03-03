package LongestPalindromicSubstring;

public class LongestPalindromic {

    public static void main(String[] args) {
        System.out.println("result: " + longestPalindromeDP("babad"));
    }

    private int lo, maxLen;

    public String longestPalindrome2(String s) {
        int len = s.length();
        if (len < 2)
            return s;

        for (int i = 0; i < len-1; i++) {
            extendPalindrome(s, i, i);  //assume odd length, try to extend Palindrome as possible
            extendPalindrome(s, i, i+1); //assume even length.
        }
        return s.substring(lo, lo + maxLen);
    }

    private void extendPalindrome(String s, int j, int k) {
        while (j >= 0 && k < s.length() && s.charAt(j) == s.charAt(k)) {
            j--;
            k++;
        }
        if (maxLen < k - j - 1) {
            lo = j + 1;
            maxLen = k - j - 1;
        }
    }

    public static String longestPalindromeDP(String s) {
        int n = s.length();
        String res = null;

        boolean[][] dp = new boolean[n][n];

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);

                if (dp[i][j] && (res == null || j - i + 1 > res.length())) {
                    res = s.substring(i, j + 1);
                }
            }
        }

        return res;
    }

    public static String longestPalindrome(String s) {
        return helper(s, 0, s.length());
    }

    public static String helper(String s, int start, int end) {
        if(start == end) {
            return "";
        }

        String current = s.substring(start, end);
        if(checkPalindrome(current)) {
            return current;
        }
        String left = helper(s, start + 1, end);
        String right = helper(s, start, end - 1);

        return left.length() > right.length() ? left : right;
    }

    public static boolean checkPalindrome(String s) {
        boolean ret = true;
        for(int i = 0; i < s.length() / 2; i++) {
            if(s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
