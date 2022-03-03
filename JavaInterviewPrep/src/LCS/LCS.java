package LCS;

import java.util.Arrays;

/**
 * Given two sequences, find the length of longest subsequence present in both of them.
 *
 * A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
 *
 * For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
 */
public class LCS {
    public static void main(String[] args) {
        String s1 = "ABCDGH";
        String s2 = "AEDFHR"; //ADH
        System.out.println("result: " + lcs(s1, s2));


        String s3 = "AGGTAB";
        String s4 = "GXTXAYB"; //GTAB
        System.out.println("result: " + lcs(s3, s4));
    }

    /* Returns length of LCS for X[0..m-1], Y[0..n-1] */
    static int lcs( char[] X, char[] Y, int m, int n )
    {
        int L[][] = new int[m+1][n+1];

        /* Following steps build L[m+1][n+1] in bottom up fashion. Note
             that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] */
        for (int i=0; i<=m; i++)
        {
            for (int j=0; j<=n; j++)
            {
                System.out.println(Arrays.toString(L[i]));
                if (i == 0 || j == 0)
                    L[i][j] = 0;
                else if (X[i-1] == Y[j-1])
                    L[i][j] = L[i-1][j-1] + 1;
                else
                    L[i][j] = max(L[i-1][j], L[i][j-1]);
            }
            System.out.println();
        }
        return L[m][n];
    }

    public static int lcs(String s1, String s2) {
        return lcs(s1.toCharArray(), s2.toCharArray(), s1.length(), s2.length());
    }

    /* Utility function to get max of 2 integers */
    static int max(int a, int b)
    {
        return (a > b)? a : b;
    }


    public static int lcsSpaceOptimized(String X, String Y) {

        // Find lengths of two strings
        int m = X.length(), n = Y.length();

        int L[][] = new int[2][n + 1];

        // Binary index, used to index
        // current row and previous row.
        int bi = 0;

        for (int i = 0; i <= m; i++) {

            // Compute current binary index
            bi = i & 1;

            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    L[bi][j] = 0;

                else if (X.charAt(i - 1) ==
                        Y.charAt(j - 1))
                    L[bi][j] = L[1 - bi][j - 1] + 1;

                else
                    L[bi][j] = Math.max(L[1 - bi][j],
                            L[bi][j - 1]);
            }
        }

        // Last filled entry contains length of
        // LCS for X[0..n-1] and Y[0..m-1]
        return L[bi][n];
    }


}
