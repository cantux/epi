package zeroMatrix;

import java.util.Arrays;

public class zeroMatrix {
    public static void main(String[] args) {

        int[][] matrix = {
                {0, 0, 0},
                {0, 0, 0},
                {0, 0, 0}
        };

        int[][] matrix1 = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        int[][] matrix2 = {
                {0, 4, 1},
                {8, 5, 2},
                {3, 6, 9}
        };
        int[][] matrix3 = {
                {1, 0, 1},
                {8, 5, 2},
                {3, 6, 9}
        };

        int[][] matrix4 = {
                {3, 8, 0},
                {6, 5, 4},
                {9, 2, 1}
        };
        int[][] matrix5 = {
                {3, 8, 3},
                {6, 0, 4},
                {9, 2, 1}
        };
        int[][] matrix6 = {
                {3, 8, 3},
                {6, 7, 4},
                {9, 2, 0}
        };

        int[][] matrix7 = {
                {3, 8, 3},
                {6, 7, 4},
                {9, 2, 0}
        };

        System.out.println("correct: " + Arrays.deepEquals(zero(matrix1, 3, 3), matrix1));
        System.out.println("correct: " + Arrays.deepEquals(zero(matrix2, 3, 3), matrix));
        System.out.println("correct: " + Arrays.deepEquals(zero(matrix3, 3, 3), matrix));
        System.out.println("correct: " + Arrays.deepEquals(zero(matrix4, 3, 3), matrix));
        System.out.println("correct: " + Arrays.deepEquals(zero(matrix5, 3, 3), matrix));
        System.out.println("correct: " + Arrays.deepEquals(zero(matrix6, 3, 3), matrix));
        System.out.println("correct: " + Arrays.deepEquals(zero(matrix7, 3, 3), matrix));
        System.out.println("correct: " + Arrays.deepEquals(zero(matrix7, 3, 3), matrix1));

    }

    public static int[][] zero(int[][] x, int m, int n) {
        for(int i = 0; i < x.length; i++)
        {
            for (int j = 0; j < x[0].length; j++)
            {
                if(x[i][j] == 0)
                {
                    return new int[x.length][x[0].length];
                }
            }
        }
        return x;
    }
}
