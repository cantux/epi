package PerfectSquares;

public class PerfectSquares {
    public int numSquares(int n) {
        if (n <= 3)
            return n;

        int min = n;
        for(int i = 1; i < n; i++) {
            int temp = i*i;
            if (temp > n)
                break;
            min = Math.min(min, numSquares(n - temp) + 1);
        }
        return min;
    }

    // Returns count of minimum squares that sum to n
    static int getMinSquares(int n)
    {
        if(n < 4) return n;

        int dp[] = new int[n+1];

        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;

        for (int i = 4; i <= n; i++)
        {
            // max value is i as i can always be represented
            // as 1*1 + 1*1 + ...
            dp[i] = i;

            // Go through all smaller numbers to
            // to recursively find minimum
            for (int x = 1; x <= i; x++) {
                int temp = x*x;
                if (temp > i)
                    break;
                else dp[i] = Math.min(dp[i], 1+dp[i-temp]);
            }
        }

        // Store result and free dp[]
        int res = dp[n];

        return res;
    }
}
