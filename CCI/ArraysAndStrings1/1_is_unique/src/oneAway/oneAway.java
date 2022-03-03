package oneAway;

import javafx.util.Pair;

import java.util.ArrayList;

public class oneAway {
    public static void main(String[] args) {
        ArrayList<Pair<String, String>> testList = new ArrayList<>();
        testList.add(new Pair<>("", ""));
        testList.add(new Pair<>("a", "a"));
        testList.add(new Pair<>("a", "b"));

        testList.add(new Pair<>("ba", "ba"));

        testList.add(new Pair<>("az", "a"));

        testList.add(new Pair<>("ab", "az"));

        testList.add(new Pair<>("ab", "a"));

        testList.add(new Pair<>("abc", "abcz"));
        testList.add(new Pair<>("abc", "zabc"));
        testList.add(new Pair<>("abc", "abzc"));

        testList.add(new Pair<>("abc", "ab"));
        testList.add(new Pair<>("abc", "bc"));
        testList.add(new Pair<>("abc", "ac"));

        testList.add(new Pair<>("abc", "abz"));
        testList.add(new Pair<>("abc", "zbc"));
        testList.add(new Pair<>("abc", "azc"));

        testList.add(new Pair<>("abc", "axz"));
        testList.add(new Pair<>("abc", "xzc"));
        testList.add(new Pair<>("abc", "abxz"));
        testList.add(new Pair<>("abc", "xzbc"));
        testList.add(new Pair<>("abc", "xyz"));

        testList.add(new Pair<>("abc", "abcasdf"));

        for (Pair<String, String> a : testList) {
            System.out.println("Result for 2N str1: " + a.getKey() + " str2: " + a.getValue() + " is: " + check(a.getKey(), a.getValue()));
            System.out.println("Result for 2N str1: " + a.getKey() + " str2: " + a.getValue() + " is: " + checkOneAway(a.getKey(), a.getValue()));
        }
    }

    public static boolean check(String str1, String str2) {
        String s1, s2;

        int strLengthDiff = str1.length() - str2.length();

        if(Math.abs(strLengthDiff) > 1) {
            return false;
        }
        else if(strLengthDiff < 0) {
            s1 = str2;
            s2 = str1;
        }
        else {
            s1 = str1;
            s2 = str2;
        }

        char[] s1c = s1.toCharArray();
        char[] s2c = s2.toCharArray();

        int i = 0;
        int j = 0;
        boolean foundDifference = false;
        while(i < s1c.length && j < s2c.length) {
            if(s1c[i] != s2c[j]) {
                if(foundDifference) {
                    return false;
                }
                foundDifference = true;
                if(s1c.length != s2c.length){
                    i++;
                }
                else {
                    i++; j++;
                }
            }
            else {
                i++; j++;
            }
        }

        return true;
    }

    public static boolean checkOneAway(String str1, String str2) {
        boolean encountered = false;
        int strLengthDiff = str1.length() - str2.length();
        if(strLengthDiff == 0) {
            for(int i = 0; i < str1.length(); i++)
            {
                boolean problem = str1.charAt(i) != str2.charAt(i);
                if(problem && encountered) {
                    return false;
                }
                else if(problem)
                {
                    encountered = true;
                }
            }
        }
        else if(strLengthDiff > 1 || strLengthDiff < -1)
        {
            return false;
        }
        else
        {
            boolean encounteredDifference = false;
            int i = 0, j = 0;
            // solve the problem for addition only and swap the longer one
            String tempstr1, tempstr2;
            if(str1.length() < str2.length()) {
                tempstr1 = str1;
                tempstr2 = str2;
            }
            else
            {
                tempstr1 = str2;
                tempstr2 = str1;
            }
            while (i < tempstr1.length() && j < tempstr2.length())
            {
                boolean mismatch = tempstr1.charAt(i) != tempstr2.charAt(j);
                if(mismatch) {
                    if(encounteredDifference) {
                        return false;
                    }
                    // if it is an addition increment
                    if(j+1 < tempstr2.length() && tempstr1.charAt(i) == tempstr2.charAt(j+1))
                    {
                        j++;
                    }
                    encounteredDifference = true;
                }
                else
                {
                    i++;
                    j++;
                }
            }

        }
        return true;
    }
}
