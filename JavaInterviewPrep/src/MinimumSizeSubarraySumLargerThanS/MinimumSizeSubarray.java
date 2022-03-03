package MinimumSizeSubarraySumLargerThanS;

public class MinimumSizeSubarray {
    // find
    int minSubArrayLen(int s, int[] nums) {
        int start = 0, end = 0;
        int minLen = Integer.MAX_VALUE, sum = 0;
        while(end < nums.length)
        {
            if(sum < s) {
                sum += nums[end];
            }

            end++;

            while(sum >= s) {
                minLen = Math.min(minLen, end - start);
                sum -= nums[start];
                start++;
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}
