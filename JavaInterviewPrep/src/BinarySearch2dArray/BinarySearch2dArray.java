package BinarySearch2dArray;

import java.util.Arrays;

public class BinarySearch2dArray {
    public static void main(String[] args) {
        int[][] arr = new int[][] {
                {10, 20, 30, 40},
                {15, 25, 31, 45},
                {25, 29, 32, 48},
                {33, 34, 39, 50},
        };
//        binarySearch(arr, 33);
        int[][] a = new int[4][4];

        int z = 0;
        for(int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                a[i][j] = z++;
            }
        }

        for(int k = 0; k < 4; k++) {
            System.out.println(Arrays.toString(a[k]));
        }

        for(int l = 0; l < 4; l++) {
            for(int m = l; m < 4; m++) {
                int temp = a[l][m];
                a[l][m] = a[m][l];
                a[m][l] = temp;
            }
        }

        for(int k = 0; k < 4; k++) {
            System.out.println(Arrays.toString(a[k]));
        }
    }

    public static void binarySearch(int[][] mat, int x) {
        int n = mat.length;
        int i = 0, j = n-1; //set indexes for top right element
        while ( i < n && j >= 0 )
        {
            System.out.println("i: " + i + " j: " + j);
            if ( mat[i][j] == x )
            {
                System.out.print("n Found at "+ i + " " + j);
                return;
            }
            if ( mat[i][j] > x )
                j--;
            else // if mat[i][j] < x
                i++;
        }
        System.out.print("n Element not found");
    }
}
