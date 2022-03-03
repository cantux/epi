package NumberOfPossibleBinarySearchTrees;

public class NoOfBST {
    public static void main(String[] args) {
        System.out.println("numTrees(1): " + numTrees(1));
        System.out.println("numTreesIterative(1): " + numTreesIterative(1));

        System.out.println("numTrees(1): " + numTrees(2));
        System.out.println("numTreesIterative(1): " + numTreesIterative(2));

        System.out.println("numTrees(1): " + numTrees(3));
        System.out.println("numTreesIterative(1): " + numTreesIterative(3));

        System.out.println("numTrees(1): " + numTrees(4));
        System.out.println("numTreesIterative(1): " + numTreesIterative(4));

        System.out.println("numTrees(1): " + numTrees(5));
        System.out.println("numTreesIterative(1): " + numTreesIterative(5));
    }

    public static int numTrees(int n) {
        int[] memo = new int[n+1];
        return numTrees(n, memo);
    }

    public static int numTrees(int n, int[] memo) {
        if(n <= 1) {
            return 1;
        }
        if(memo[n] > 0) {
            return memo[n];
        }

        // trick with "<="
        for(int i = 1; i <= n; i++) {
            memo[n] += numTrees(n - i, memo) * numTrees(i - 1, memo);
        }

        return memo[n];
    }

    public static int numTreesIterative(int n) {
        int[] memo = new int[n + 1];
        memo[0] = 1;
        memo[1] = 1;
        for(int i = 2; i <= n; i++){
            for(int j = 1; j <= i; j++) {
                memo[i] += memo[i - j] * memo[j - 1];
            }
        }

        return memo[n];
    }

}
