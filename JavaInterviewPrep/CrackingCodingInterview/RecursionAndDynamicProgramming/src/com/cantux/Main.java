package com.cantux;

public class Main {

    public static void main(String[] args) {
        for(int i = 0; i < 5; i++) {
            System.out.println("fib: i: " + i + " is: " + fib(i));
        }
//
//        for(int i = 0; i < 5; i++) {
//            System.out.println("fact: i: " + i + " is: " + fact(i));
//        }

        long startNormFib = System.currentTimeMillis();
        System.out.println("norm fib: " + fib(40));
        long endNormFib = System.currentTimeMillis();
        System.out.println("memo fib: " + fibonacci(40));
        long endMemoFib = System.currentTimeMillis();
        System.out.println("tab fib: " + fibTab(40));
        long endTabFib = System.currentTimeMillis();
        System.out.println("normal fib took: " + (endNormFib - startNormFib));
        System.out.println("memo fib took: " + (endNormFib - endMemoFib));
        System.out.println("memo fib took: " + (endMemoFib - endTabFib));

    }

    public static int fact(int number) {
        if(number == 0) {
            return 1;
        }
        return number * fact(number -1);
    }

    public static int fib(int number) {
        if(number == 0) {
            return 0;
        }
        else if(number == 1) {
            return 1;
        }
        return fib(number - 1) + fib(number - 2);
    }

    public static int fibonacci(int number) {
        return fibonacciMemo(number, new int[number + 1]);
    }

    public static int fibonacciMemo(int number, int[] memo) {
        if(number == 0 || number == 1) return number;
        if(memo[number] == 0) {
            memo[number] = fibonacciMemo(number - 1, memo) + fibonacciMemo(number - 2, memo);
        }
        return memo[number];
    }

    public static int fibTab(int n) {
        int[] dp = new int[n + 1];

        dp[0] = 0;
        dp[1] = 1;

        for(int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }
}
