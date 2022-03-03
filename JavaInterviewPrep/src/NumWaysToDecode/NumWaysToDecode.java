package NumWaysToDecode;

import java.util.HashMap;
import java.util.Map;


public class NumWaysToDecode {

    public static void main(String [] args) {
        Solution s = new Solution();

        long start1 = System.currentTimeMillis();
        long result = s.numWays("6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155");
        long finish1 = System.currentTimeMillis();
        System.out.println("time: " + (finish1 - start1) + " ways: " + result);

        Map<String, Long> hs = new HashMap();
        long start2 = System.currentTimeMillis();
        long x = s.numWays("6065812287883668764831544958683283296479682877898293612168136334983851946827579555449329483852397155", hs);
        long finish2 = System.currentTimeMillis();
        System.out.println("time: " + (finish2 - start2) + " ways: " + x);
     }

    static class Solution {
//        public int numDecodings(String s) {
//            Box b = new Box();
//            numDecodings(s, s.length(), b);
//            return b.count;
//        }
//
//        public boolean numDecodings(String s, int length, Box b) {
//            if(s.length() == 1) {
//                b.count++;
//                return true;
//            }
//            else if(s.length() == 2 && Integer.valueOf(s) <= 26) {
//                b.count++;
//                return numDecodings(s.substring(1), length - 1, b);
//            }
//            else if(numDecodings(s.substring(1), length - 1, b)) {
//                return true;
//            }
//            else if(numDecodings(s.substring(2), length -2, b) && Integer.valueOf(s.substring(0,2)) <= 26) {
//                return true;
//            }
//            return false;
//        }
//
//        protected class Box {
//            public int count = 0;
//        }

        public long numWays(String s){
            if(s == null || s.length() == 0) {
                return 0;
            }
            int n = s.length();
            int[] dp = new int[n+1];
            dp[0] = 1;
            dp[1] = s.charAt(0) != '0' ? 1 : 0;
            for(int i = 2; i <= n; i++) {
                int first = Integer.valueOf(s.substring(i-1, i));
                int second = Integer.valueOf(s.substring(i-2, i));
                if(first >= 1 && first <= 9) {
                    dp[i] += dp[i-1];
                }
                if(second >= 10 && second <= 26) {
                    dp[i] += dp[i-2];
                }
            }
            return dp[n];

        }

        public long numWays(String s, Map<String, Long> hs) {
            if(s.length() == 0){
                return 0;
            }
            else if(s.length() == 1) {
                if(Integer.valueOf(s) == 0) {
                    return 0;
                }
                return 1;
            }
            else if (s.length() == 2 && Integer.valueOf(s) <= 26) {
                return 2;
            }
            if(hs.containsKey(s)) {
                return hs.get(s);
            }
            long result = numWays(s.substring(1), hs) + numWays(s.substring(2), hs);
            hs.put(s, result);
            return result;
        }
    }
}
