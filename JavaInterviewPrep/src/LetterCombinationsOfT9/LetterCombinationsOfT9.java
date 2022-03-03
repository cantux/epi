package LetterCombinationsOfT9;

import java.util.ArrayList;
import java.util.List;

public class LetterCombinationsOfT9 {

    public static void main(String[] args) {
        System.out.println("Result: " + letterCombinations("23"));
    }

    public static String[] t9 = new String[]{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public static List<String> letterCombinations(String digits) {
        if(digits.length() == 0) return new ArrayList();
        int n = digits.length();

        List<String> letterList = new ArrayList();

        for(int i = 0; i < n; i++) {
            String letters = t9[digits.charAt(i) - '0'];
            letterList.add(letters);
        }

        List<String> retList = new ArrayList();

        helper(letterList, 0, letterList.size(), "", retList);

        return retList;
    }

    static void helper(List<String> letterList, int currentListIndex, int listSize, String runStr, List<String> retList) {
        if(currentListIndex == listSize) {
            retList.add(runStr);
            return;
        }
        String currentChars = letterList.get(currentListIndex);
        for(int i = 0; i < currentChars.length(); i++) {
            helper(letterList, currentListIndex + 1, listSize, runStr + currentChars.charAt(i), retList);
        }
    }

}
