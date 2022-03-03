package GraphBipartite;

import java.util.*;

public class GraphBipartite {
    public static void main(String[] args) {
        int[][] graphDef1 = new int[][] {
                {1,3}, {0,2}, {1,3}, {0,2}
        };
        System.out.println("Result 1: " + isBipartite(graphDef1));

        int[][] graphDef2 = new int[][] {
                {1,2,3}, {0,2}, {0,1,3}, {0,2}
        };
        System.out.println("Result 2: " + isBipartite(graphDef2));
    }

    public static boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        Arrays.fill(color, -1);

        for (int start = 0; start < n; ++start) {
            if (color[start] == -1) {
                Stack<Integer> stack = new Stack();
                stack.push(start);
                color[start] = 0;

                while (!stack.empty()) {
                    Integer node = stack.pop();
                    for (int nei: graph[node]) {
                        if (color[nei] == -1) {
                            stack.push(nei);
                            color[nei] = color[node] ^ 1;
                        } else if (color[nei] == color[node]) {
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
}
