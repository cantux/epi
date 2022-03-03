package FindPivotIndex;

import java.util.Arrays;

/**
 * Given an array of integers nums, write a method that returns the "pivot" index of this array.
 *
 * We define the pivot index as the index where the sum of the numbers to the left of the index
 * is equal to the sum of the numbers to the right of the index.
 *
 * If no such index exists, we should return -1. If there are multiple pivot indexes,
 * you should return the left-most pivot index.
 */
public class FindPivotIndex {
    public static void main(String[] args) {
        int[] test1 = new int[]{5, 4, 3, 2, 1, 2, 3, 4, 5};
        System.out.println(findPivot(test1));
        int[] test2 = new int[]{5, 1, 5};
        System.out.println(findPivot(test2));

        System.out.println(pivotIndex(test1));
        System.out.println(pivotIndex(test2));
    }

    public static int pivotIndex(int[] nums) {
        int total = 0, sum = 0;
        for (int num : nums) {
            total += num;
        }
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sum * 2 == total - nums[i]) {
                return i;
            }
        }

        return -1;
    }

    public static int findPivot(int[] arr) {
        int[] newArr = new int[arr.length];
        newArr[0] = arr[0];
        for(int i = 1; i < arr.length; i++) {
            newArr[i] = newArr[i-1] + arr[i];
        }

        System.out.println("new arr: " + Arrays.toString(newArr));

        return findMedian(newArr, 0, newArr.length - 1);
    }

    public static int findMedian(int[] arr, int begin, int end) {
        if(begin == end) {
            return end;
        }
        int mid = (begin + end) / 2;

        if(arr[mid+1] == arr[end] - arr[mid]) {
            return mid;
        }
        else if(arr[mid+1] < arr[end] - arr[mid]) {
            return findMedian(arr, mid, end);
        }
        else {
            return findMedian(arr, begin, mid);
        }
    }
}
