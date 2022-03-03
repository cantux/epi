package RotateArray;

import java.util.*;

public class RotateArray {

    public static void main(String []args){
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};

        rotate(arr, 5);
        // [6, 7, 8, 9, 1, 2, 3, 4, 5]
        //   [5, 4, 3, 2, 1, 6, 7, 8, 9]
        //   [5, 4, 3, 2, 1, 9, 8, 7, 6]
        //   [6, 7, 8, 9, 1, 2, 3, 4, 5]

        System.out.println("resut: " + Arrays.toString(arr));
    }
    public static void rotate(int[] arr, int k) {
        k = k % arr.length;
        reverse(arr, 0, k - 1);
        reverse(arr, k, arr.length - 1);
        reverse(arr, 0, arr.length - 1);
    }
    public static void reverse(int[] arr, int left, int right) {
        int l=left, r=right;
        while (l < r) {
            swap(arr, l, r);
            l++;
            r--;
        }
    }
    public static void swap(int[] arr, int l, int r) {
        int temp = arr[l];
        arr[l] = arr[r];
        arr[r] = temp;
    }
}
