package MaximumSizeSubarraySumEqualsK;

import java.util.HashMap;
import java.util.Map;

/**
 * create the sums avalanche as expected again. Also put the values and indeces into a Map
 *
 * we are given the target sum. So while iterating through the array, if there is a subarray ever, the map must contain
 * sum - targetSum
 */
public class MaximumSizeSubarraySumEqualsK {

    public int maxSubArrayLen(int[] nums, int targetSum) {
        int sum = 0, max = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            sum = sum + nums[i];

            // instead of checking for equality, we can push a Entry(0, 0)
            if (sum == targetSum) {
                max = i + 1;
            } else if (map.containsKey(sum - targetSum)) {
                max = Math.max(max, i - map.get(sum - targetSum));
            }

            if (!map.containsKey(sum)) {
                map.put(sum, i);
            }
        }
        return max;
    }
}
