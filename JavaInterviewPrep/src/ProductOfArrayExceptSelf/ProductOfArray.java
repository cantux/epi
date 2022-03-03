package ProductOfArrayExceptSelf;

import java.util.Arrays;

/**
 * Given an array nums of n integers where n > 1,
 *
 * return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
 */

// traverse from the start and end
public class ProductOfArray {
    public static void main(String[] args) {
        int[] arr = new int[]{1,2,3,4};
        System.out.println("Reustl: " + Arrays.toString(productExceptSelf(arr)));
    }

    public static int[] productExceptSelf(int[] nums) {
        int[] ret = new int[nums.length];

        ret[0] = 1;
        for(int i = 1; i < nums.length; i++) {
            ret[i] = nums[i - 1] * ret[i-1];
        }
        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            ret[i] *= right;
            right *= nums[i];
        }
        return ret;
    }
}
