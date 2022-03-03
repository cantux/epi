package WordLadder;

import java.util.*;

public class WordLadder {
    public static void main(String[] args) {
        List<String> wordList = new ArrayList();

        wordList.add("hot");
        wordList.add("dot");
        wordList.add("dog");
        wordList.add("lot");
        wordList.add("log");
        wordList.add("cog");

        System.out.println("result: " + ladderLength("hit", "cog", wordList));
    }

    public static int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(wordList.size() == 0) return -1;

        // All words have the same length

        // brute force solution
        // find the neighbors of the current word in the list
        // find the neighbors of the neighbor while increasing count.
        // return as we find the solution immediately

        // we will be stuck in a loop in this solution if we don't mark the visited neighbors.

        Set<String> words = new HashSet(wordList);
        Set<String> visited = new HashSet();

        Queue<String> q = new LinkedList();

        q.add(beginWord);

        int level = 0;

        while(!q.isEmpty()) {

            String s = q.poll();

            level++;

            visited.add(s);
            Set<String> neighbors = findNeighbors(s, words);
            System.out.println(neighbors);
            for(String neighbor: neighbors) {
                if(neighbors.contains(endWord)) {
                    return level;
                }
                if (!visited.contains(neighbor)) {
                    q.add(neighbor);
                }
            }
        }

        return 0;
    }

    public static Set<String> findNeighbors(String beginWord, Set<String> words) {
        Set<String> retSet = new HashSet();
        char[] chs = beginWord.toCharArray();
        for (int i = 0; i < chs.length; i++) {
            char temp = chs[i];
            for (char c = 'a'; c <= 'z'; c++) {
                chs[i] = c;
                String tryWord = new String(chs);
                if(words.contains(tryWord)) {
                    retSet.add(tryWord);
                }
            }
            chs[i] = temp;
        }
        return retSet;
    }
}
