package PowerSet;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class PowerSet {
    public static void main(String[] args) {
        int[] test0 = new int[] {1,2,3};

        System.out.println("result: " + subSet(test0));
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        for(int n : nums){
            int size = result.size();
            for(int i=0; i<size; i++){
                // MAGIC HERE, get the ith result!!
                List<Integer> subset = new ArrayList<>(result.get(i));
                subset.add(n);
                result.add(subset);
            }
        }
        return result;
    }

    public static List<List<Integer>> subSet(int[] arr) {
        List<List<Integer>> allLists = new LinkedList<>();
        subSet(arr, 0, arr.length, new LinkedList(), allLists);
        return allLists;
    }

    // idea is to create a binary decision tree of sizeof(array)
    public static void subSet(int[] arr, int count, int limit, List<Integer> list, List<List<Integer>> allLists) {
        if(count == limit) {
            allLists.add(list);
            return;
        }

        List<Integer> tempList = new LinkedList<>(list);
        subSet(arr, count + 1, limit, tempList, allLists);

        List<Integer> tempList2 = new LinkedList<>(list);
        tempList2.add(arr[count]);
        subSet(arr, count + 1, limit, tempList2, allLists);
    }


    public static ArrayList<ArrayList<Integer>> getSubsets(ArrayList<Integer> set, int index) {
        ArrayList<ArrayList<Integer>> allSubsets;
        if(set.size() == index) {
            allSubsets = new ArrayList<>();
            allSubsets.add(new ArrayList());
        }
        else {
            allSubsets = getSubsets(set, index + 1);

            int item = set.get(index);

            ArrayList<ArrayList<Integer>> moreSubsets = new ArrayList();

            for(ArrayList<Integer> subset: allSubsets) {
                ArrayList<Integer> newSubset = new ArrayList(subset);
                newSubset.add(item);
                moreSubsets.add(newSubset);
            }
            allSubsets.addAll(moreSubsets);
        }
        return allSubsets;
    }
}
