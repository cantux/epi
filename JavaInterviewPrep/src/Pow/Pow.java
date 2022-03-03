package Pow;

/**
 * Given an integer x and a positive number y, write a function that computes xy under following conditions.
 * a) Time complexity of the function should be O(Log y)
 * b) Extra Space is O(1)
 */
public class Pow {
    static int power(int x, int y)
    {
        if (y == 0)
            return 1;
        else if (y % 2 == 0)
            return power(x, y / 2) * power(x, y / 2);
        else
            return x * power(x, y / 2) * power(x, y / 2);
    }

    public static void main(String[] args)
    {
        int x = 2;
        int y = 3;

        System.out.printf("%d", power(x, y));
    }
}
