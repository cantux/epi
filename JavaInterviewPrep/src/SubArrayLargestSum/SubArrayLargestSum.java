package SubArrayLargestSum;

import java.util.Arrays;

public class SubArrayLargestSum {

    public static void main(String[] args) {

        int[] a0 = new int[]{1, 2, 3, 4, 5, 6};

        int[] a1 = new int[]{1, -2, 1, 1};

        int[] a2 = new int[]{1};

        int[] a3 = new int[]{-2, 2, 3, 4};

        int[] a4 = new int[]{-2, -1, 0};

        int[] a5 = new int[]{100, -5, -10};
    }

    public static int maxContinuousSubArray(int[] A) {
        int maxSoFar=A[0], maxEndingHere=A[0];

        for (int i=1;i<A.length;++i){
            maxEndingHere = Math.max(maxEndingHere+A[i],A[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
    }

    public static int maxSubArray(int[] A) {
        int max = Integer.MIN_VALUE, sum = 0;
        for (int i = 0; i < A.length; i++) {
            if (sum < 0)
                sum = A[i];
            else
                sum += A[i];
            if (sum > max)
                max = sum;
        }
        return max;
    }
}
