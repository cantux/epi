package stringRotation;

import javafx.util.Pair;

import java.util.ArrayList;

public class stringRotation {
    public static void main(String[] args) {
        ArrayList<Pair<String, String>> testList = new ArrayList<>();

        testList.add(new Pair<>("", ""));
        testList.add(new Pair<>("a", "a"));
        testList.add(new Pair<>("ab", "ab"));
        testList.add(new Pair<>("ab", "ba"));

        testList.add(new Pair<>("abc", "cab"));
        testList.add(new Pair<>("abc", "bca"));
        testList.add(new Pair<>("aaa", "aaa"));

        testList.add(new Pair<>("abca", "aabc"));

        testList.add(new Pair<>("aba", "bab"));

        for (Pair<String, String> a : testList) {
            System.out.println("Result for 2N str1: " + a.getKey() + " str2: " + a.getValue() + " is: " + isStringRotation(a.getKey(), a.getValue()));
        }
    }

    public static boolean isStringRotation(String str1, String str2) {
        if(str1.length() == str2.length()) {
            String strCombination = str1 + str1;
            return strCombination.contains(str2);
        }

        return false;
    }
}
