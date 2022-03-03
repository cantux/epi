package WordBreak;

import javafx.util.Pair;

import java.util.*;

public class WordBreak {
    public static void main(String[] args) {
        ArrayList<Pair<String, Set<String>>> list = new ArrayList<>();

        HashSet<String> hs0 = new HashSet<>();
        hs0.add("leet");
        hs0.add("code");

        Pair<String, Set<String>> testPair0 = new Pair("leetcode", hs0);
        Pair<String, Set<String>> testPair1 = new Pair("leecode", hs0);
        Pair<String, Set<String>> testPair2 = new Pair("leetode", hs0);
        Pair<String, Set<String>> testPair3 = new Pair("leectode", hs0);

        list.add(testPair0);
        list.add(testPair1);
        list.add(testPair2);
        list.add(testPair3);

        for (Pair<String, Set<String>> pair : list) {
            System.out.println("String: " + pair.getKey());
            System.out.println("Set: " + pair.getValue());
            System.out.println("Result: " + wordBreakMemoization(pair.getKey(), pair.getValue()));
            System.out.println("Result: " + wordBreakBFS(pair.getKey(), pair.getValue()));
            System.out.println("Result: " + wordBreakDP(pair.getKey(), pair.getValue()));
        }

    }

    // dp[partitionStartIndex][partitionLength]
    public static boolean wordBreakMemoization(String word, Set<String> dict) {
        return word_Break(word, dict, 0, new Boolean[word.length()]);
    }

    public static boolean word_Break(String s, Set<String> wordDict, int start, Boolean[] memo) {
        if (start == s.length()) {
            return true;
        }
        if (memo[start] != null) {
            return memo[start];
        }
        for (int end = start + 1; end <= s.length(); end++) {
            if (wordDict.contains(s.substring(start, end)) && word_Break(s, wordDict, end, memo)) {
                return memo[start] = true;
            }
        }
        return memo[start] = false;
    }

    public static boolean wordBreakBFS(String s, Set<String> wordDict) {
        Queue<Integer> queue = new LinkedList<>();
        int[] visited = new int[s.length()];
        queue.add(0);
        while (!queue.isEmpty()) {
            int start = queue.remove();
            if (visited[start] == 0) {
                for (int end = start + 1; end <= s.length(); end++) {
                    if (wordDict.contains(s.substring(start, end))) {
                        queue.add(end);
                        if (end == s.length()) {
                            return true;
                        }
                    }
                }
                visited[start] = 1;
            }
        }
        return false;
    }

    public static boolean wordBreakDP(String s, Set<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordDict.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}
