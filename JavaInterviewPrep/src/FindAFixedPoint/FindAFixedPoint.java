package FindAFixedPoint;


/** value equal to index **/
public class FindAFixedPoint {
    public static void main(String[] args) {

    }

    public int fixedPoint(int[] arr) {
        return fixedPoint(arr, 0, arr.length);
    }

    public static int fixedPoint(int[] arr, int begin, int end) {
        if(begin > end) {
            return -1;
        }
        int mid = (begin + end) / 2;

        if(arr[mid] == mid) {
            return mid;
        }
        else if(arr[mid] > mid) {
            return fixedPoint(arr, mid, end);
        }
        return fixedPoint(arr, begin, mid);
    }
}
