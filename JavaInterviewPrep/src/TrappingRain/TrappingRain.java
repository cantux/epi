package TrappingRain;

public class TrappingRain {

    public static void main(String[] args) {
        int[] arr = new int[] {
                0,1,0,2,1,0,1,3,2,1,2,1
        };

        System.out.println("result: " + trap(arr));
    }

    static int trap(int[] arr) {
        int ans = 0;
        int length = arr.length;

        for(int i = 1; i < length - 1; i++) {
            int max_left = 0, max_right = 0;

            for(int j = i; j >= 0; j--) {
                max_left = Math.max(max_left, arr[j]);
            }

            for(int j = i; j < length; j++) {
                max_right = Math.max(max_right, arr[j]);
            }

            ans += Math.min(max_left, max_right) - arr[i];
        }

        return ans;
    }

    static int trapDp(int[] height) {
        int ans = 0;
        int size = height.length;
        int[] left_max = new int[size];
        int[] right_max = new int[size];
        left_max[0] = height[0];
        for (int i = 1; i < size; i++) {
            left_max[i] = Math.max(height[i], left_max[i - 1]);
        }
        right_max[size - 1] = height[size - 1];
        for (int i = size - 2; i >= 0; i--) {
            right_max[i] = Math.max(height[i], right_max[i + 1]);
        }
        for (int i = 1; i < size - 1; i++) {
            ans += Math.min(left_max[i], right_max[i]) - height[i];
        }
        return ans;
    }
}
