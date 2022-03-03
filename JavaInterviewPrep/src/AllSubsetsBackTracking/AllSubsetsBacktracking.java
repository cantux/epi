package AllSubsetsBackTracking;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AllSubsetsBacktracking {

    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        subsets(list, new ArrayList<>(), nums, 0);
        return list;
    }

    private static void subsets(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
        list.add(new ArrayList<>(tempList));
        for(int i = start; i < nums.length; i++){
            tempList.add(nums[i]);
            subsets(list, tempList, nums, i + 1);
            tempList.remove(tempList.size() - 1);
        }
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        subsetsWithDup(list, new ArrayList<>(), nums, 0);
        return list;
    }

    private void subsetsWithDup(List<List<Integer>> list, List<Integer> tempList, int [] nums, int start){
        list.add(new ArrayList<>(tempList));
        for(int i = start; i < nums.length; i++){
            if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates
            tempList.add(nums[i]);
            subsetsWithDup(list, tempList, nums, i + 1);
            tempList.remove(tempList.size() - 1);
        }
    }
}
