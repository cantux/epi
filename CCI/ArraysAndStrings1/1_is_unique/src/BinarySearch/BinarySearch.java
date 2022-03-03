package BinarySearch;

public class BinarySearch {

    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5};

    }

    public static int binarySearch(int[] array, int value, int index, int length) {
        if(length == 1) {
            return array[index] == value ? index : -1;
        }
        if(array[index] == value)
        {
            return index;
        }
        else if(array[index] < value) {
            return binarySearch(array, value, index/2, length / 2);
        }
        else {
            return binarySearch(array, value, index + index/2, length / 2);
        }
    }
}
