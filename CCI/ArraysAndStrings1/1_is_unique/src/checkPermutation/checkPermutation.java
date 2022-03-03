package checkPermutation;

import javafx.util.Pair;
import java.util.ArrayList;
import java.util.HashSet;

public class checkPermutation {

    public static void main(String[] args) {
        ArrayList<Pair<String, String>> testList = new ArrayList<>();

        testList.add(new Pair<>("a", "a"));
        testList.add(new Pair<>("aabb", "abab"));
        testList.add(new Pair<>("abc", "cba"));

        testList.add(new Pair<>("a", "b"));
        testList.add(new Pair<>("aabb", "aaa"));
        testList.add(new Pair<>("abc", "bbb"));

        for (Pair<String, String> a : testList) {
            System.out.println("Result for 2N str1: " + a.getKey() + " str2: " + a.getValue() + " is: " + checkPerm(a.getKey(), a.getValue()));
        }
    }

    public static boolean checkPerm(String str1, String str2) {
        HashSet<Character> hs = new HashSet<>();
        int str1Length = str1.length();
        int str2Length = str2.length();
        if(str1Length != str2Length) {
            return false;
        }
        if(str1Length == 1) {
            return str1.equals(str2);
        }

        for (int i = 0; i < str1Length; i++) {
            hs.add(str1.charAt(i));
        }

        for (int i = 0; i < str2Length; i++) {
            hs.remove(str2.charAt(i));
        }

        return hs.isEmpty() || hs.size() == 1;
    }

}