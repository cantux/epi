package BurstBaloons;

public class BurstBaloons {
    public static void main(String[] args) {

    }

    public static int maxCoins(int[] nums) {
        int n = nums.length;
        if(n == 0) return 0;
        if(n == 1) return nums[0];

        int[][] coin = new int[n + 2][n + 2];

        int[] list = new int[n + 2];
        list[0] = 1;
        list[n + 1] = 1;

        for(int i = 0; i < n; i++){
            list[i + 1] = nums[i];
        }

        for(int len = 1; len <= n; len++){
            for(int i = 1; i <= n - len + 1 ; i++){
                int j = len + i - 1;
                for(int k = i; k <= j; k++){
                    coin[i][j] = Math.max(coin[i][j],
                            coin[i][k - 1] + list[i - 1]* list[k] * list[j + 1] + coin[k + 1][j]);
                }
            }
        }
        return coin[1][n];
    }
}
