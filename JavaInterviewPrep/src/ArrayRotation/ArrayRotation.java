package ArrayRotation;

import java.util.Arrays;

public class ArrayRotation {
    public static void main(String[] args) {
        int[] arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = i;
        }

        for(int j = 0; j < 3; j++) {
            leftRotateArray1(arr, j);
            System.out.println(Arrays.toString(arr));
        }
    }

    public static void leftRotateArray1(int[] arr, int rot) {
        for(int i = 0; i < rot; i++) {
            leftRotatebyOne(arr);
        }
    }

    public static void leftRotatebyOne(int[] arr) {
        int i, temp;
        temp = arr[0];
        for(i = 0; i < arr.length - 1; i++) {
            arr[i] = arr[i+1];
        }
        arr[i] = temp;
    }

    public static void rotateArray2(int[] arr, int rot) {
        int i, j, k, temp;
        int arrayLength = arr.length;
        for (i = 0; i < gcd(rot, arrayLength); i++)
        {
            /* move i-th values of blocks */
            temp = arr[i];
            j = i;
            while (true)
            {
                k = j + rot;
                if (k >= arrayLength)
                    k = k - arrayLength;
                if (k == i)
                    break;
                arr[j] = arr[k];
                j = k;
            }
            arr[j] = temp;
        }
    }

    public static int gcd(int a, int b)
    {
        if (b == 0)
            return a;
        else
            return gcd(b, a % b);
    }
}