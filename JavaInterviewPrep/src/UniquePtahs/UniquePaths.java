package UniquePtahs;

public class UniquePaths {
    public static void main(String[] args) {
        System.out.println("result  " + uniquePaths(new int[][] {
            {0,0,0},
            {0,1,0},
            {0,0,0}
        }));
    }

    public static int uniquePaths(int[][] obstacleGrid) {
        int rowSize = obstacleGrid.length;
        int colSize;
            if(rowSize == 0) {
            return 0;
        }
            else {
            colSize = obstacleGrid[0].length;
            if(colSize == 0) {
                return 1;
            }
            else {
                int[][] ways = new int[rowSize][colSize];
                return helper(obstacleGrid, 0, rowSize, 0, colSize, ways);
            }
        }
    }

    public static int helper(int[][] obstacleGrid, int currentRow, int maxRow, int currentCol, int maxCol, int[][] dp) {
        dp[0][0] = obstacleGrid[0][0] == 1 ? 0 : 1;
        for (int i = 1; i < maxRow; i++) {
            if (obstacleGrid[i][0] == 1) {
                dp[i][0] = 0;
                continue;
            }
            dp[i][0] = dp[i - 1][0];
        }

        for (int i = 1; i < maxCol; i++) {
            if (obstacleGrid[0][i] == 1) {
                dp[0][i] = 0;
                continue;
            }
            dp[0][i] = dp[0][i - 1];
        }

        for (int i = 1; i < maxRow; i++) {
            for (int j = 1; j < maxCol; j++) {
                if(obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }

        return dp[maxRow - 1][maxCol - 1];
    }
}
