package MaxOfTheRotatedArrays;

public class MaxOfTheRotatedArrays {

    public static void main(String[] args) {
        int[] arr = new int[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = i;
        }

        char[] c = new char[]{'a','a'};

        String s = new String(c);

        System.out.println("reult : " +maxOfTheRotated(arr));
        int[] arr2 = new int[] {4,3,2,6};
        System.out.println("reult : " +maxOfTheRotated(arr2));
    }

    public static int maxOfTheRotated(int[] arr) {
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < arr.length; i++) {
            int currentSum = 0;
            for(int j = 0; j < arr.length; j++) {
                currentSum += j * arr[j];
            }
            max = Math.max(currentSum, max);
            leftRotateArray1(arr, 1);
        }

        return max;
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
}
