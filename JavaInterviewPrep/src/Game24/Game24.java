package Game24;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Game24 {
    public static double epsilon = .00001;

    public static void main(String[] args) {
        int[] arr = new int[] {1, 2, 3, 4};

        System.out.println("result: " + judgePoint241(arr));
    }

    final static double eps = 0.001;

    public static boolean judgePoint241(int[] nums) {
        List<Double> arr = new ArrayList<>();
        for(int n: nums) arr.add((double) n);
        Boolean res = new Boolean(false);
        helper1(arr, res);
        return res;
    }

    private static void helper1(List<Double> arr, Boolean res){
        if(res) return;
        if(arr.size() == 1){
            if(Math.abs(arr.get(0) - 24.0) < eps)
                res = true;
            return;
        }
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < i; j++) {
                List<Double> next = new ArrayList<>();
                Double p1 = arr.get(i), p2 = arr.get(j);
                next.addAll(Arrays.asList(p1+p2, p1-p2, p2-p1, p1*p2));
                if(Math.abs(p2) > eps)  next.add(p1/p2);
                if(Math.abs(p1) > eps)  next.add(p2/p1);

                arr.remove(i);
                arr.remove(j);
                for (Double n: next){
                    arr.add(n);
                    helper1(arr, res);
                    arr.remove(arr.size()-1);
                }
                arr.add(j, p2);
                arr.add(i, p1);
            }
        }
    }

    ///////////////////////////////////////

    public static boolean judgePoint24(int[] nums) {
        double[] data = new double[nums.length] ;
        for (int i = 0; i < nums.length; i++) data[i] = (double) nums[i];
        return helper(data);
    }

    private static boolean helper(double[] nums) {

        if (nums.length == 1) return Math.abs(nums[0]- 24.0) < 0.0001;

        // create a new double[] whose length is 1 smaller than that of nums
        int n = nums.length;
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {

                // initialize double[] for dfs and set its part of entries
                double[] next = new double[n-1];
                for(int k = 0, index = 0; k < n; k++) {
                    if (k != i && k != j) next[index++] = nums[k];
                }

                double d1 = nums[i], d2 = nums[j];

                // get all possible operation results from nums[i] and nums[j] then dfs
                // the last entry in 'next' is next[n-2]
                double[] dirs = new double[]{d1 + d2, d1 - d2, d2 - d1, d2 * d1};
                for (double dir: dirs) {
                    next[n-2] = dir;
                    if (helper(next)) return true;
                }

                if (d1 > 0.0001) {
                    next[n-2] = d2 / d1;
                    if (helper(next)) return true;
                }

                if (d2 > 0.0001) {
                    next[n-2] = d1 / d2;
                    if (helper(next)) return true;
                }
            }
        }

        return false;
    }



}
