package PatternMatching;

import java.util.Arrays;

public class PatternMatching {
    public static void main(String[] args) {

    }
//
//    public boolean patternMatch(String str, String pattern) {
//        Map<Character, Integer> charMap = new HashMap();
//        for(int i = 0; i< pattern.length(); i++) {
//            char pc = pattern.charAt(i);
//            charMap.put(pattern.charAt(i), charMap.getOrDefault(pc, 0) + 1);
//        }
//
//    }

    static int countSol(int coeff[],
                        int n, int rhs)
    {

        // Create and initialize a table to
        // store results of subproblems
        int dp[] = new int[rhs + 1];
        Arrays.fill(dp, 0);
        dp[0] = 1;

        // Fill table in bottom up manner
        for (int i = 0; i < n; i++)
            for (int j = coeff[i]; j <= rhs; j++)
                dp[j] += dp[j - coeff[i]];

        return dp[rhs];
    }
}
