package MostCommonWord;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class MostCommonWord {
    public static void main(String[] args) {
        String[] banned = new String[] {"hit"};
        System.out.println("resutl: " + mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned));
    }

    public static String mostCommonWord(String paragraph, String[] banned) {
        String[] splitArr = paragraph.replaceAll("[!?',;.]","").toLowerCase().split(" ");

        Set<String> bannedSet = new HashSet();
        for(String s: banned) {
            bannedSet.add(s);
        }

        Map<String, Integer> hm = new HashMap();
        for(int i = 0; i < splitArr.length; i++) {
            String splitWord = splitArr[i];
            if(!bannedSet.contains(splitWord)) {
                hm.put(splitWord, hm.getOrDefault(splitWord, 0) + 1);
            }
        }

        Set<Map.Entry<String, Integer>> es = hm.entrySet();

        int max = Integer.MIN_VALUE;
        String word = "";
        for(Map.Entry<String,Integer> me: es) {
            int val = me.getValue();
            if(val > max) {
                word = me.getKey();
            }
            max = Math.max(val, max);
        }
        return word;
    }
}
