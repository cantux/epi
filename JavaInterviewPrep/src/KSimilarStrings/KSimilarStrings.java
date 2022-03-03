package KSimilarStrings;

import java.util.*;

public class KSimilarStrings {

    public int kSimilarity(String A, String B) {
        Queue<String> queue = new LinkedList<>();
        Set<String> seen = new HashSet<>();
        queue.offer(A);
        seen.add(A);
        int res = 0;
        while (!queue.isEmpty()){
            int size = queue.size();
            for (int i = 0; i < size; i++){
                String curr = queue.poll();
                if (curr.equals(B)){
                    return res;
                }
                int j = 0;
                while (j < curr.length() && curr.charAt(j) == B.charAt(j)){
                    j++;
                }
                for (int k = j + 1; k < curr.length(); k++){
                    if (curr.charAt(k) == B.charAt(j) && curr.charAt(k) != B.charAt(k)){
                        String next = swap(curr, j, k);//return string to ensure that curr won't change
                        if (!seen.contains(next)){
                            queue.offer(next);
                            seen.add(next);
                        }
                    }
                }
            }
            res++;
        }
        return res;
    }
    private String swap(String curr, int j, int k){
        char[] arr = curr.toCharArray();
        char temp = arr[j];
        arr[j] = arr[k];
        arr[k] = temp;
        return new String(arr);
    }
}
