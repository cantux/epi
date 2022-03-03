package TwoSum;


import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static void main(String[] args) {
        int[] s = findSum(new int[]{3,2,4}, 6);
        System.out.println("result: " + s[0] + s[1]);
    }

    public static int[] findSum(int[] nums, int target) {
        Map<Integer, Integer> s = new HashMap();
        for(int i = 0; i < nums.length; i++) {
            int x = target - nums[i];
            if(s.containsKey(x)){
                return new int[]{ s.get(x), i };
            }
            s.put(nums[i], i);
        }

        return null;
    }
}
