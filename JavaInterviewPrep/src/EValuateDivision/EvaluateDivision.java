package EValuateDivision;

import java.util.*;

public class EvaluateDivision {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        Map<String, Map<String, Double>> adjList = new HashMap<>();

        int eqLength = equations.length;
        for(int i = 0; i < eqLength; i++) {
            String from = equations[i][0];
            String to = equations[i][1];
            Map<String, Double> fromTo = adjList.getOrDefault(from, new HashMap<String, Double>());
            fromTo.put(to, Double.valueOf(values[i]));
            adjList.put(from, fromTo);

            Map<String, Double> toFrom = adjList.getOrDefault(to, new HashMap<String, Double>());
            toFrom.put(from, 1 / Double.valueOf(values[i]));
            adjList.put(to, toFrom);
        }

        int queryLength = queries.length;
        double[] ret = new double[queryLength];
        for(int i = 0; i < queryLength; i++) {
            String start = queries[i][0];
            String end = queries[i][1];
            Set<String> visited = new HashSet<>();
            visited.add(start);
            ret[i] = dfs(adjList, start, end, 1, visited);
        }

        return ret;
    }

    double dfs(Map<String, Map<String, Double>> adjList, String current, String target, double soFar, Set<String> visited) {
        Map<String, Double> neighbors = adjList.get(current);
        double ret = -1;
        if(neighbors != null) {
            for(Map.Entry<String, Double> entry: neighbors.entrySet()) {
                String currentNeighbor = entry.getKey();
                double currentRatio = entry.getValue();
                if(currentNeighbor.equals(target)) {
                    return soFar * currentRatio;
                }
                if(!visited.contains(currentNeighbor)) {
                    visited.add(currentNeighbor);
                    double temp = dfs(adjList, currentNeighbor, target, soFar * currentRatio, visited);
                    if(temp != -1) {
                        ret = temp;
                    }
                }
            }
        }

        return ret;
    }
}
