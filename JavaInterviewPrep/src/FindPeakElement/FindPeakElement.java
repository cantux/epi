package FindPeakElement;

import java.util.Arrays;

public class FindPeakElement {
    public static void main(String[] args) {
        int[] ab = new int[]{1,2,1};
        System.out.println("result : " + peak(ab));

        int[] a = new int[]{1,2,1,3,1};
        System.out.println("result : " + peak(a));

        int[] c = new int[]{1};
        System.out.println("result : " + peak(c));

        int[] b = new int[]{1,2,3,4,5,6,7,8,9};
        System.out.println("result : " + peak(b));

        int[] d = new int[]{1,2,3,5,4,6,7,8};
        System.out.println("result : " + peak(d));

        int[] e = new int[]{1,2,3,5,4,3,2,1};
        System.out.println("result : " + peak(e));

    }

    public static int findPeak(int[] arr) {
        int oneBefore = 0;
        int[] diffArr = new int[arr.length];
        for(int i = 0; i < arr.length; i++) {
            diffArr[i] = arr[i] - oneBefore;
            oneBefore = arr[i];
        }

        for(int i = 1; i < arr.length; i++) {
            if(diffArr[i] < 0 && diffArr[i - 1] > 0) {
                return i - 1;
            }
        }
        return arr.length - 1;
    }

    public static int peak(int[] arr) {
        if(arr.length <= 1) {
            return 0;
        }
        return helper(arr, 0, arr.length - 1);
    }
    public static int helper(int[] arr, int low, int high) {
        if(low == high) {
            return low;
        }

        int mid = (low + high) / 2;
        if(arr[mid] <= arr[mid+1]) {
            return helper(arr, mid + 1, high);
        }
        else {
            return helper(arr, low, mid);
        }
    }
}
