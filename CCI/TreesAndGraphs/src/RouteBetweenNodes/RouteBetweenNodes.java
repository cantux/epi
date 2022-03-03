package RouteBetweenNodes;


import Graph.IntegerGraph;

import java.util.Iterator;

public class RouteBetweenNodes extends IntegerGraph {
    public static void main(String[] args) {

        RouteBetweenNodes g = new RouteBetweenNodes (7);

        g.addUndirectedEdge(0,1);
        g.addUndirectedEdge(1,2);
        g.addUndirectedEdge(2,3);

        g.addUndirectedEdge(1,4);

        g.addUndirectedEdge(3,4);
        g.addUndirectedEdge(4,5);
        g.addUndirectedEdge(5,0);

        System.out.println("Is there a route: " + g.routeBetweenNodes(0, 3));
        System.out.println("Is there a route: " + g.routeBetweenNodes(0, 6));
    }

    public RouteBetweenNodes(int size) {
        super(size);
    }

    public boolean routeBetweenNodes(int src, int dest) {
        boolean[] visited = new boolean[super.size];
        return rbnHelper(src, dest, visited, false);
    }

    public boolean rbnHelper(int src, int dest, boolean[] visited, boolean found) {
        visited[src] = true;

        if(src == dest) {
            return true;
        }
        Iterator<Integer> it = super.adjListArray[src].listIterator();
        while(it.hasNext()) {
            int n = it.next();
            if(!visited[n]) {
                found = found || rbnHelper(n, dest, visited, found);
            }
        }
        return found;
    }

}
