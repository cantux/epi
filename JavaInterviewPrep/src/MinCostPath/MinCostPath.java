package MinCostPath;

import java.util.Arrays;

public class MinCostPath {

    public static void main(String[] args) {
        int cost[][] = { {1, 2, 3},
                {4, 8, 2},
                {1, 5, 3} };

        System.out.println(minCost(cost, 2, 2));
        System.out.println(minCost(cost, 1, 1));
    }

    public static int minCost(int[][] cost, int row, int col) {
        int[][] dp = new int[row + 1][col + 1];

        dp[0][0] = cost[0][0];
        /* Initialize first column of total cost(tc) array */
        for (int i = 1; i <= row; i++)
            dp[i][0] = dp[i-1][0] + cost[i][0];

        /* Initialize first row of tc array */
        for (int j = 1; j <= col; j++)
            dp[0][j] = dp[0][j-1] + cost[0][j];


        for(int i = 0; i < row + 1; i++)
            System.out.println(Arrays.toString(dp[i]));

        for(int i = 1; i < row + 1; i++) {
            for(int j = 1; j < col+ 1; j++) {
                dp[i][j] = cost[i][j] + Math.min(dp[i - 1][j], Math.min(dp[i][j - 1], dp[i - 1][j -1]));
            }
        }

        for(int i = 0; i < row + 1; i++)
            System.out.println(Arrays.toString(dp[i]));

        return dp[row][col];
    }
}
