package MergeSortedArray.MergeSortedArrayInplace;

import java.util.Arrays;

/** Startint from the end is the trick **/
public class MergeSorted {
    public static void main(String[] args) {
        int[] arr1 = {2,9,14};
        int[] arr2 = {13,18,-1,-1,-1};

        merge(arr2,arr1);

        System.out.println("result0: " + Arrays.toString(arr2));

        int[] arr3 = {1,2,3,0,0,0};
        int[] arr4 = {2,5,6};

        merge(arr3,arr4);

        System.out.println("result1: " + Arrays.toString(arr3));
    }
    public static void merge(int[] nums1, int[] nums2) {
        merge(nums1, nums1.length, nums2, nums2.length);
    }

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int fp = m - n - 1, sp = n - 1, endP = m - 1;
        while(fp >= 0 && sp >= 0) {
            if(nums2[sp] >= nums1[fp]) {
                nums1[endP] = nums2[sp];
                sp--;
            }
            else{
                nums1[endP] = nums1[fp];
                fp--;
            }
            endP--;
        }
        if(sp > fp) {
            while(endP >= 0) {
                nums1[endP] = nums2[endP];
                endP--;
            }
        }
    }
}
