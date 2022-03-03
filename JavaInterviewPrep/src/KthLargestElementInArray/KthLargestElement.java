package KthLargestElementInArray;

import java.util.ArrayList;

import java.util.PriorityQueue;
import java.util.Random;

public class KthLargestElement {
    public static void main(String [] args ) {
        ArrayList<int[]> list = new ArrayList<>();

        list.add(new int[]{1, 2, 3, 4, 5, 6});
        for(int[] arr : list) {
            System.out.println("result: " + kthLargestElement(arr, 4));
            System.out.println("qs part: " + findKthLargestQSPart(arr, 4));
            System.out.println("qs rand: " + findKthLargestQSPartRandomized(arr, 4));
        }
    }

    public static int kthLargestElement(int[] arr, int k) {

        final PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int val : arr) {
            pq.offer(val);

            if(pq.size() > k) {
                pq.poll();
            }
        }
        return pq.peek();
    }

    public static int findKthLargestQSPart(int[] nums, int k) {

        k = nums.length - k;
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            final int j = partition(nums, lo, hi);
            if(j < k) {
                lo = j + 1;
            } else if (j > k) {
                hi = j - 1;
            } else {
                break;
            }
        }
        return nums[k];
    }

    private static int partition(int[] a, int lo, int hi) {

        int i = lo;
        int j = hi + 1;
        while(true) {
            while(i < hi && less(a[++i], a[lo]));
            while(j > lo && less(a[lo], a[--j]));
            if(i >= j) {
                break;
            }
            exch(a, i, j);
        }
        exch(a, lo, j);
        return j;
    }

    private static void exch(int[] a, int i, int j) {
        final int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    private static boolean less(int v, int w) {
        return v < w;
    }


    public static int findKthLargestQSPartRandomized(int[] nums, int k) {
        shuffle(nums);
        k = nums.length - k;
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            final int j = partition(nums, lo, hi);
            if(j < k) {
                lo = j + 1;
            } else if (j > k) {
                hi = j - 1;
            } else {
                break;
            }
        }
        return nums[k];
    }

    private static void shuffle(int a[]) {

        final Random random = new Random();
        for(int ind = 1; ind < a.length; ind++) {
            final int r = random.nextInt(ind + 1);
            exch(a, ind, r);
        }
    }
}
