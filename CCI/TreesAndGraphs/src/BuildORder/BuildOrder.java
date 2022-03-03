package BuildORder;

import Graph.IntegerGraph;

import java.util.HashMap;

public class BuildOrder {
    public static void main(String[] args) {
        //projects
        String[] projects = new String[] { "a", "b", "c", "d", "e", "f"};
        String[][] dependencies = new String[][] {
                {"d"},
                {"d"},
                {},
                {"c"},
                {},
                {"a", "b"}
        };

        HashMap<String, Integer> nodesMap = new HashMap();
        for(int i = 0; i < projects.length; i++) {
            nodesMap.put(projects[i], i);
        }

        IntegerGraph g = new IntegerGraph(projects.length);

        for(int i = 0; i < dependencies.length; i++) {
            for(int j = 0; j < dependencies[i].length; j++){
                System.out.println("dep: " + dependencies[i][j]);
                System.out.println("mapped to: " + nodesMap.get(dependencies[i][j]));
                g.addDirectedEdge(i, nodesMap.get(dependencies[i][j]));
            }
        }

        g.topologicalSort();
    }


}
