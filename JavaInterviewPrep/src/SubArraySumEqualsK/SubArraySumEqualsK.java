package SubArraySumEqualsK;

import java.util.HashMap;
import java.util.Map;

public class SubArraySumEqualsK {
    public static void main(String[] args) {
//        int[] a = new int[]{10, 20, 30, 40, 50};
//        System.out.println("result: " + subArraySum(a, 10));
//        System.out.println("result: " + subArraySum(a, 150));
//        System.out.println("result: " + subArraySum(a, 60));
//        System.out.println("result: " + subArraySum(a, 50));
//        System.out.println("result: " + subArraySum(a, 30));
//
//        int[] b = new int[]{50, 40, 30, 20, 10};
//        System.out.println("result: " + subArraySum(b, 10));
//        System.out.println("result: " + subArraySum(b, 150));
//        System.out.println("result: " + subArraySum(b, 60));
//        System.out.println("result: " + subArraySum(b, 50));
//        System.out.println("result: " + subArraySum(b, 30));
//
//        int[] c = new int[]{30, 20, 10, 40, 50};
//        System.out.println("result: " + subArraySum(c, 10));
//        System.out.println("result: " + subArraySum(c, 150));
//        System.out.println("result: " + subArraySum(c, 60));
//        System.out.println("result: " + subArraySum(c, 50));
//        System.out.println("result: " + subArraySum(c, 30));
//
//        int[] d = new int[]{40, 50};
//        System.out.println("result: " + subArraySum(d, 90));
//        System.out.println("result: " + subArraySum(d, 40));
//        System.out.println("result: " + subArraySum(d, 50));

        int[] e = new int[]{1};
        System.out.println("result: " + subArraySum(e, 0));
    }

    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int[] sum = new int[nums.length + 1];
        sum[0] = 0;
        for (int i = 1; i <= nums.length; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        for (int start = 0; start < nums.length; start++) {
            for (int end = start + 1; end <= nums.length; end++) {
                if (sum[end] - sum[start] == k)
                    count++;
            }
        }
        return count;
    }

    public int subarraySum2(int[] nums, int k) {
        int count = 0, sum = 0;
        HashMap < Integer, Integer > map = new HashMap < > ();
        map.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }

    public static int subArraySum(int[] arr, int k) {
        int arrSize = arr.length;
        int[] sumArray = new int[arrSize];
        sumArray[0] = arr[0];
        for(int i = 1; i < arrSize; i++) {
            sumArray[i] = sumArray[i - 1] + arr[i];
        }

        Map<Integer, Integer> hm = new HashMap<>();
        for(int j = 0; j < arrSize; j++) {
            hm.put(sumArray[j], j);
        }

        int countResult = 0;
        for(Map.Entry<Integer, Integer> entry: hm.entrySet()) {
            int expected = entry.getKey() - k;
            if(hm.containsKey(expected) || expected == 0) {
                countResult++;
            }
        }
        return countResult;
    }
}
