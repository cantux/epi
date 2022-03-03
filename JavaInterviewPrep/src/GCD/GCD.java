package GCD;

public class GCD {
    public static void main(String[] args) {
        System.out.println(gcd(100,4));
    }

    public static int gcd(int x, int y) {
        int m, n;

        /* x > 0 and y > 0 */
        m = x; n = y;
        while (m != n)
        {
            if(m>n)
                m = m - n;
            else
                n = n - m;
        }
        return n;
    }

    static int gcd1(int a, int b)
    {
        if (b == 0)
            return a;
        return gcd1(b, a % b);
    }

    static int gcd2(int a, int b)
    {
        // Everything divides 0
        if (a == 0 || b == 0)
            return 0;

        // base case
        if (a == b)
            return a;

        // a is greater
        if (a > b)
            return gcd2(a-b, b);
        return gcd2(a, b-a);
    }
}
