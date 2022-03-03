package MinimumWindowSubstring.SmallestWindow;

import java.util.*;

public class SmallestWindow {
    public static void main(String[] args) {
        System.out.println("result: " + g("this is a test string", "tist"));
        System.out.println("result: " + g("geeksforgeeks", "ork"));

//        System.out.println("what: " + checkAllExists("this is a test string", getFreqMap("tist")));
    }

    public static Map getFreqMap(String b) {
        Map<Character, Integer> hm = new HashMap();

        for(int j = 0; j < b.length(); j++) {
            char c = b.charAt(j);
            hm.put(c, hm.getOrDefault(c, 0) + 1);
        }
        return hm;
    }

    public static String g(String a, String b) {
        Map<Character, Integer> hm = getFreqMap(b);

        int minStart = 0, minEnd = 0, minLength = Integer.MAX_VALUE;
        for(int i = 0; i < a.length(); i++) {
            for(int j = i; j < a.length(); j++) {
                if(checkAllExists(a.substring(i, j), hm)) {
                    if(j - i < minLength) {
                        minStart = i;
                        minEnd = j;
                        minLength = j - i;
                    }
                }
            }
        }
        return a.substring(minStart, minEnd);
    }

    public static boolean checkAllExists(String s, Map<Character, Integer> hm){
        Map<Character, Integer> map = new HashMap(hm);

        for(int i = 0; i< s.length(); i++) {
            char c = s.charAt(i);
            if(map.containsKey(c)) {
                map.put(c, map.get(c) - 1);
            }
        }

        for(int i: map.values()) {
            if(i > 0) {
                return false;
            }
        }
        return true;
    }

}
