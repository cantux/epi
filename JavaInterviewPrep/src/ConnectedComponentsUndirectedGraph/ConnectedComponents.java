package ConnectedComponentsUndirectedGraph;

import java.util.*;

public class ConnectedComponents {
    public static void main(String[] args) {
        int[][] edges1 = new int[][] {
                {0, 1}, {1, 2}, {3, 4}
        };
        System.out.println("Result 1 : " + countComponents(5, edges1));

        int[][] edges2 = new int[][] {
                {0, 1}, {1, 2}, {2, 3}, {3, 4}
        };
        System.out.println("Result 2 : " + countComponents(5, edges2));
    }

    public static int countComponents(int n, int[][] edges) {
        if (n <= 1)
            return n;
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            map.get(edge[0]).add(edge[1]);
            map.get(edge[1]).add(edge[0]);
        }
        Set<Integer> visited = new HashSet<>();
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (visited.add(i)) {
                dfsVisit(i, map, visited);
                count++;
            }
        }
        return count;
    }


    private static void dfsVisit(int i, Map<Integer, List<Integer>> map, Set<Integer> visited) {
        for (int j : map.get(i)) {
            if (visited.add(j))
                dfsVisit(j, map, visited);
        }
    }
}
