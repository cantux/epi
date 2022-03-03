package RodCutting;

public class RodCutting {

    static int cutRod(int price[], int n) {
        if (n <= 0) {
            return 0;
        }

        int max = Integer.MIN_VALUE;
        for (int i = 1; i < n && i < price.length; i++) {
            max = Math.max(max, price[i] + cutRod(price, n - i - 1));
        }
        return max;
    }

    /* Driver program to test above functions */
    public static void main(String args[])
    {
        int arr[] = new int[] {0, 1, 5, 8, 9, 10, 17, 17, 20};
        int size = arr.length;
        System.out.println("Maximum Obtainable Value is "+
                cutRod(arr, 10));

    }

    public static int maxValueCuts(int left, int[] dat) {
        if(left == 0) {
            return 0;
        }

        int max = Integer.MIN_VALUE;

        for(int i = 1; i < left && i < dat.length; i++) {
            max = Math.max(max, dat[i] + maxValueCuts(left - i, dat));
        }

        return max;
    }

    static int cutRodDP(int price[],int n)
    {
        int val[] = new int[n+1];
        val[0] = 0;

        // Build the table val[] in bottom up manner and return
        // the last entry from the table
        for (int i = 1; i<=n; i++)
        {
            int max_val = Integer.MIN_VALUE;
            for (int j = 0; j < i; j++)
                max_val = Math.max(max_val,
                        price[j] + val[i-j-1]);
            val[i] = max_val;
        }

        return val[n];
    }
}
