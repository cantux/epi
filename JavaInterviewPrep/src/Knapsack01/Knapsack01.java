package Knapsack01;

public class Knapsack01 {

    static int max(int a, int b) { return (a > b)? a : b; }

    static int knapSack(int W, int wt[], int val[], int n)
    {
        if (n == 0 || W == 0)
            return 0;

        // If weight of the nth item is more than Knapsack capacity W, then
        // this item cannot be included in the optimal solution
        if (wt[n-1] > W)
            return knapSack(W, wt, val, n-1);

            // Return the maximum of two cases:
            // (1) nth item included
            // (2) not included
        else return max( val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                knapSack(W, wt, val, n-1)
        );
    }

    // tricks,
    // - we know that dp dimensions are [values][W]
    // - recurrence: dp[v][w] =  dp[i-1][w - weights[w - weights[i - 1]]]
    static int tuxDpKnapSack(int W, int wt[], int val[], int n)
    {
        int i, w;
        int K[][] = new int[n+1][W+1];

        // Build table K[][] in bottom up manner
        for (i = 0; i <= n; i++)
        {
            for (w = 0; w <= W; w++)
            {
                if (i==0 || w==0)
                    K[i][w] = 0;
                else if (wt[i-1] <= w)
                    K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]);
                else
                    K[i][w] = K[i-1][w];
            }
        }

        return K[n][W];
    }
    public static void main(String args[])
    {
        int val[] = new int[]{60, 100, 120};
        int wt[] = new int[]{10, 20, 30};
        int  W = 50;
        int n = val.length;
        System.out.println(knapSack(W, wt, val, n));
        System.out.println(tuxDpKnapSack(W, wt, val, n));

        int val1[] = new int[]{24, 18, 18, 10};
        int wt1[] = new int[]{24, 10, 10, 7};
        int  W1 = 25;
        int n1 = val.length;
        System.out.println(knapSack(W1, wt1, val1, n1));
        System.out.println(tuxDpKnapSack(W1, wt1, val1, n1));
    }
}
