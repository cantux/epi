package PositionOfLargeGroups;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class PositionOfLargeGroups {

    public static void main(String[] args){
//        System.out.println("result: " + largeGroupPositions("aabbbcc"));
//        System.out.println("result: " + largeGroupPositions("abbxxxxzzy"));
//        System.out.println("result: " + largeGroupPositions("abc"));
        System.out.println("result: " + largeGroupPositions("aaa"));

    }

    public List<List<Integer>> largeGroupPositions(String S, int k) {
        int i = 0, j = 0, N = S.length();
        List<List<Integer>> res = new ArrayList<>();
        while (j < N) {
            while (j < N && S.charAt(j) == S.charAt(i)) ++j;
            if (j - i >= 3) res.add(Arrays.asList(i, j - 1));
            i = j;
        }
        return res;
    }

    public static List<List<Integer>> largeGroupPositions(String s) {
        List<List<Integer>> returnList = new ArrayList<>();

        char[] arr = s.toCharArray();

        int currentCount = 0, minPosition = 10000, maxPosition = 0;
        for(int i = 1; i < arr.length; i++) {
            if(arr[i] == arr[i-1]) {
                currentCount++;
                minPosition = Math.min(minPosition, i - 1);
                maxPosition = Math.max(maxPosition, i);
            }
            else {
                if(maxPosition - minPosition > 1) {
                    List<Integer> beginEndList = new LinkedList();
                    beginEndList.add(minPosition);
                    beginEndList.add(maxPosition);
                    returnList.add(beginEndList);
                }
                currentCount = 0;
                minPosition = 10000;
                maxPosition = 0;
            }
        }

        return returnList;
    }
}
