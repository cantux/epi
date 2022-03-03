package SlidingWindowMaximum;

import java.util.*;

public class SlidingWindowMaximum {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0) return new int[0];
        Deque<Integer> d = new ArrayDeque<>();
        int[] result = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            //discard values lower than current
            while (!d.isEmpty() && nums[d.peekLast()] < n) {
                d.removeLast();
            }
            //discard right-most index of previous window
            if (!d.isEmpty() && d.peekFirst() == i - k) {
                d.pop();
            }

            //add current
            d.add(i);

            //skip over the first window
            if (i < k - 1) {
                continue;
            }

            //head of d contains the max value over the window
            result[i - k + 1] = nums[d.peekFirst()];
        }
        return result;
    }
}
