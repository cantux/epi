package TopKFrequentWords;

import java.util.*;

/**
 * Given a non-empty list of words, return the k most frequent elements.
 *
 * Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
 * then the word with the lower alphabetical order comes first.
 */
public class TopKFrequentWords {
    public static void main(String[] args) {
        String[] arr = new String[] {"i", "love", "leetcode", "i", "love", "coding"};
        System.out.println("result: " + topKFrequent(arr, 2));
    }
    public static List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> map = new HashMap<>();
        for(String n: words){
            map.put(n, map.getOrDefault(n,0)+1);
        }

        PriorityQueue<Map.Entry<String, Integer>> maxHeap =
                new PriorityQueue<>((a, b)->(b.getValue()-a.getValue()));
        for(Map.Entry<String,Integer> entry: map.entrySet()){
            maxHeap.add(entry);
        }

        List<String> res = new ArrayList<>();
        while(res.size()<k){
            Map.Entry<String, Integer> entry = maxHeap.poll();
            res.add(entry.getKey());
        }
        return res;
    }
}
