package MaxConsequitive1s;

public class MaxConsequitive1s {
    public static void main(String[] args) {
        int[] arr = new int[]{1,1,1,1,1,0,1,1,1,1};
        System.out.println("resutl: " + maxCons1s(arr));
    }

    public static int maxCons1s(int[] arr) {
        int max = 0;

        int currentCount = 0;

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == 0) {
                currentCount = 0;
            }
            else if(arr[i] == 1) {
                currentCount++;
            }
            max = Math.max(max, currentCount);
        }

        return max;
    }
}
