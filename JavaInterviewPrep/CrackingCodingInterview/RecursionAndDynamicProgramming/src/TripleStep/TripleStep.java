package TripleStep;

import java.util.Arrays;

/**
 * A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time.
 * Implement a method to count how many possible ways the child can run up the stairs.
 */
public class TripleStep {
    public static void main(String[] args) {
        System.out.println("Normal count ways: " + countWays(5));
        System.out.println("Memo count ways: " + countWaysMemo(5));
    }

    public static int countWays(int n) {
        if(n < 0) {
            return 0;
        }
        else if (n == 0) {
            return 1;
        }
        else {
            return countWays(n - 1) + countWays(n - 2) + countWays(n - 3);
        }
    }

    public static int countWaysMemo(int n) {
        int[] memo = new int[n+1];
        Arrays.fill(memo, -1);
        return countWaysMemoRec(n, memo);
    }

    public static int countWaysMemoRec(int n, int[] memo) {
        if(n<0) {
            return 0;
        } else if(n == 0) {
            return 1;
        } else if(memo[n] > -1) {
            return memo[n];
        } else {
            memo[n] = countWaysMemoRec(n-1, memo) + countWaysMemoRec(n-2, memo) + countWaysMemoRec(n-3, memo);
            return memo[n];
        }
    }

}
