package ReverseArray;

public class ReverseArray {

    /* Utility that prints out an
    array on a line */
    static void printArray(int arr[],
                           int size)
    {
        for (int i = 0; i < size; i++)
            System.out.print(arr[i] + " ");

        System.out.println();
    }


    // Driver code
    public static void main(String args[]) {

        int arr[] = {1, 2, 3, 4, 5, 6};
        printArray(arr, 6);
        reverse(arr);
        System.out.print("Reversed array is \n");
        printArray(arr, 6);

    }


    public static void reverse(int[] arr) {
        int end = arr.length - 1, begin = 0;

        while(begin < end) {
            int temp = arr[begin];
            arr[begin] = arr[end];
            arr[end] = temp;
            begin++;
            end--;
        }
    }
}
