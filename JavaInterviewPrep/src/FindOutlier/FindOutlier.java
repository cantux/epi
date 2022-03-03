package FindOutlier;

import java.util.*;

// Suppose we have some input in the form of a list of lists. Each sublist has a length of at least 3.

// Each sublist consists of N elements but contains only 2 different values -- a "default" number that appears N-1 times, and an "outlier" number that only appears once. (For example, in the list [2, 2, 6, 2], the outlier is 6.)

// Write a function that, for a given list of lists, returns the outlier from each sublist. Each one is guaranteed to contain exactly one outlier.

// Sample input:


// lists = [[1, 2, 1], [2, 2, 2, 2, 2, 6, 2], [3, 1, 1, 1], [9, 9, 4]]

// # Expected output: 2, 6, 3, 4

public class FindOutlier {


    public static void main(String[] args) {
        // list of length m
        // avarage values in the lists are n, say that list lengths are uniformly distributed

        // O(m * n)
        // space complexity O(1)

        List<List<Integer>> inputLists = Arrays.asList(
                Arrays.asList(1, 2, 1),
                Arrays.asList(2, 2, 2, 2, 2, 6, 2),
                Arrays.asList(3, 1, 1, 1),
                Arrays.asList(-1, -1, -32),
                Arrays.asList(-1, -1, 0),
                Arrays.asList(-1, -1, 0),
                Arrays.asList(9, 9, 4)
        );

        // [2,6,3,4]

        System.out.println("resutls: " + findOutliers(inputLists));
    }


    public static List<Integer> findOutliers(List<List<Integer>> list) {
        List<Integer> newList = new ArrayList<Integer>();

        Iterator<List<Integer>> it = list.iterator();

        while(it.hasNext()) {
            List<Integer> inner = it.next();

            Map<Integer, Integer> m = new HashMap();

            for(int i : inner) {
                if(m.containsKey(i)) {
                    int count = m.get(i);
                    m.put(i, ++count);
                }
                else {
                    m.put(i, 1);
                }
            }

            Set<Map.Entry<Integer, Integer>> es = m.entrySet();

            Iterator<Map.Entry<Integer, Integer>> it2 = es.iterator();
            while(it2.hasNext()) {
                Map.Entry<Integer, Integer> entry = it2.next();
                if(entry.getValue() == 1) {
                    newList.add(entry.getKey());
                }
            }


        }
        return newList;
    }

}
