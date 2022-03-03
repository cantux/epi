package RegularExpressionMatching;

public class RegularExpressionMatching {
    public boolean isMatch1(String s, String p) {
        int strLength = s.length();
        int patternLength = p.length();

        if(patternLength == 0) return strLength == 0;

        boolean currentMatch = strLength > 0 && (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.');

        // if star
        // case there is no character, only move the pattern (because of "0" or more)
        // case char matches, don't move the pattern, move the str
        if(patternLength >= 2 && p.charAt(1) == '*') {
            return isMatch(s, p.substring(2)) || (currentMatch && isMatch(s.substring(1), p));
        } else {
            return currentMatch && isMatch(s.substring(1), p.substring(1));
        }
    }

    public boolean isMatch(String s, String p) {
        int strLength = s.length();
        int patternLength = p.length();

        if(patternLength == 0) return strLength == 0;
        boolean[][] dp = new boolean[strLength + 1][patternLength + 1];

        dp[strLength][patternLength] = true;

        for(int i = strLength; i >= 0; i--) {
            for(int j = patternLength - 1; j >= 0; j--) {
                boolean currentMatch = i < strLength && (p.charAt(j) == s.charAt(i) || p.charAt(i) == '.');

                if(j + 1 < patternLength && p.charAt(j) == '*') {
                    dp[i][j] = dp[i][j + 2] || currentMatch && dp[i+1][j];
                }
                else {
                    dp[i][j] = currentMatch && dp[i+1][j+1];
                }
            }
        }

        return dp[0][0];
    }
}
