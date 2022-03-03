package BinarySearchRotatedArray;

public class BinarySearchRotatedArray {
    public static void main(String[] args) {
        int[] arr = new int[] {3,4,5,1,2};
        System.out.println("result: " + bs(arr, 5));

        int[] arr1 = new int[] {3,5,1};
        System.out.println("result: " + bs(arr1, 3));
    }

    public static int bs(int[] arr, int target) {
        int start = 0, end = arr.length - 1;

        while(start <= end) {
            int mid = (start + end) / 2;
            if(arr[mid] == target) {
                return mid;
            }
            else if(arr[mid] <= arr[end]) { // case where right part of the array is sorted normally
                if(target > arr[mid] && target <= arr[end]) {
                    start = mid + 1;
                }
                else {
                    end = mid - 1;
                }
            }
            else if(arr[mid] >= arr[start]) {
                if(target < arr[mid] && target >= arr[start]) {
                    end = mid - 1;
                }
                else {
                    start = mid + 1;
                }
            }
        }

        return -1;
    }

    public static int pivotedBinarySearch(int arr[], int n, int key) {
        // how hard is it to find the max of the array? in logn?
        int pivot = findPivot(arr, 0, n-1);

        // If we didn't find a pivot, then
        // array is not rotated at all
        if (pivot == -1)
            return binarySearch(arr, 0, n-1, key);

        // If we found a pivot, then first
        // compare with pivot and then
        // search in two subarrays around pivot
        if (arr[pivot] == key)
            return pivot;
        if (arr[0] <= key)
            return binarySearch(arr, 0, pivot-1, key);
        return binarySearch(arr, pivot+1, n-1, key);
    }

    public static int findPivot(int arr[], int low, int high)
    {
        // base cases
        if (high < low)
            return -1;
        if (high == low)
            return low;

        /* low + (high - low)/2; */
        int mid = (low + high)/2;
        if (mid < high && arr[mid] > arr[mid + 1])
            return mid;
        if (mid > low && arr[mid] < arr[mid - 1])
            return (mid-1);
        if (arr[low] >= arr[mid])
            return findPivot(arr, low, mid-1);
        return findPivot(arr, mid + 1, high);
    }

    public static int binarySearch(int arr[], int low, int high, int key)
    {
        if (high < low)
            return -1;

        /* low + (high - low)/2; */
        int mid = (low + high)/2;
        if (key == arr[mid])
            return mid;
        if (key > arr[mid])
            return binarySearch(arr, (mid + 1), high, key);
        return binarySearch(arr, low, (mid -1), key);
    }
}
