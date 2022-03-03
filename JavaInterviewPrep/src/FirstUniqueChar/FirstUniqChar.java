package FirstUniqueChar;

import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

/**
 * Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
 */
public class FirstUniqChar {
    public static void main(String[] args) {

    }
    public static int firstUniqChar(String s) {

        Map<Character, Integer> singleMap = new LinkedHashMap();
        Set<Character> multipleSet = new HashSet();

        int index = 0;
        char[] charArray = s.toCharArray();
        for(int i = 0; i < charArray.length;i++) {
            char c = charArray[i];
            if(multipleSet.contains(c)) continue;
            else if(singleMap.containsKey(c)) {
                singleMap.remove(c);
                multipleSet.add(c);
            }
            else {
                singleMap.put(c, i);
            }
        }

        return singleMap.isEmpty() ? -1 : singleMap.entrySet().iterator().next().getValue();
    }
}
