package LongestConsequitiveSubsequence;

import java.util.HashMap;
import java.util.Map;

public class LongestConsequitiveSubsequence {

    public static void main(String[] args) {
        System.out.println("Result: " + ls(new int[]{25, 1,2,3,69,4}));
    }

    public static int ls(int[] arr) {
        Map<Integer, Integer> map = new HashMap();

        int n = arr.length;
        int[] dp = new int[n];

        int max = Integer.MIN_VALUE;        for(int i = 0; i < n; i++) {
            // if a[i]-1 is present before i-th index
            if (map.containsValue(arr[i] - 1)) {

                // last index of a[i]-1
                int lastIndex = map.get(arr[i] - 1) - 1;

                // relation
                dp[i] = 1 + dp[lastIndex];
            }
            else
                dp[i] = 1;

            // stores the index as 1-index as we need to
            // check for occurrence, hence 0-th index
            // will not be possible to check
            map.put(arr[i], i + 1);

            // stores the longest length
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
