package rotateMatrix;

import java.util.Arrays;

public class rotateMatrix {

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        int[][] matrixRot90 = {
                {7, 4, 1},
                {8, 5, 2},
                {3, 6, 9}
        };

        int[][] matrixRot180 = {
                {3, 8, 7},
                {6, 5, 4},
                {9, 2, 1}
        };

        System.out.println("correct: " + Arrays.deepEquals(rotate(matrix), matrixRot90));
    }

    public static int[][] rotate (int[][] inp) {
        int i = 0, j = 0;
        int[][] arr = new int[inp.length][inp.length];
        while(i < inp.length)
        {
            while(j < inp.length)
            {
                arr[inp.length - 1 - j][inp.length -1 - i] = inp[i][j];
                System.out.println(arr[inp.length - 1 - j][inp.length -1 - i]);
                j++;
            }
            i++;
        }
        return arr;
    }
}
