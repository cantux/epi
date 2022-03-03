package Graph;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class IntegerGraph {

    public static void main(String[] args) {
        IntegerGraph g = new IntegerGraph(5);

        g.addDirectedEdge(0, 1);
        g.addDirectedEdge(0, 2);
        g.addDirectedEdge(1, 3);
        g.addDirectedEdge(2, 4);

        g.BFS(0);

        g.DFS(0);

        g.topologicalSort();

        IntegerGraph g1 = new IntegerGraph(6);
        g1.addDirectedEdge(5, 2);
        g1.addDirectedEdge(5, 0);
        g1.addDirectedEdge(4, 0);
        g1.addDirectedEdge(4, 1);
        g1.addDirectedEdge(2, 3);
        g1.addDirectedEdge(3, 1);

        g1.topologicalSort();
    }

    protected int size = 0;
    protected LinkedList[] adjListArray = null;

    public IntegerGraph(int size) {
        this.size = size;
        this.adjListArray = new LinkedList[size];

        for(int i = 0; i < this.size; i++)
            this.adjListArray[i] = new LinkedList<>();
    }

    public void addUndirectedEdge(int src, int dest)
    {
        adjListArray[src].addFirst(dest);

        adjListArray[dest].addFirst(src);
    }

    void topologicalSortUtil(int v, boolean visited[],
                             Stack stack)
    {
        // Mark the current node as visited.
        visited[v] = true;
        Integer i;

        // Recur for all the vertices adjacent to this
        // vertex
        Iterator<Integer> it = adjListArray[v].iterator();
        while (it.hasNext())
        {
            i = it.next();
            if (!visited[i])
                topologicalSortUtil(i, visited, stack);
        }

        // Push current vertex to stack which stores result
        stack.push(new Integer(v));
    }

    // The function to do Topological Sort. It uses
    // recursive topologicalSortUtil()
    public void topologicalSort()
    {
        Stack stack = new Stack();

        // Mark all the vertices as not visited
        boolean visited[] = new boolean[this.size];

        // Call the recursive helper function to store
        // Topological Sort starting from all vertices
        // one by one
        for (int i = 0; i < this.size; i++)
            if (visited[i] == false)
                topologicalSortUtil(i, visited, stack);

        // Print contents of stack
        while (stack.empty()==false)
            System.out.print(stack.pop() + " ");
    }

    public void addDirectedEdge(int src, int dest)
    {
        adjListArray[src].addFirst(dest);
    }

    public void BFS(int source) {
        Queue<Integer> q = new LinkedList<>();

        boolean[] visited = new boolean[size]; // java inits bool array with falses

        visited[source] = true;
        ((LinkedList<Integer>) q).addFirst(source);

        while(q.size() != 0) {
            source = q.poll();

            System.out.println("visiting BFS node: " + source);

            Iterator<Integer> i = adjListArray[source].listIterator();
            while(i.hasNext()) {
                int n = i.next();
                if(!visited[n]) {
                    visited[n] = true;
                    q.add(n);
                }
            }
        }
    }

    public void DFS(int source) {
        boolean[] visited = new boolean[this.size];

        DFSHelper(source, visited);
    }

    public void DFSHelper(int source, boolean[] visited) {
        visited[source] = true;

        System.out.println("DFS visiting source: " + source);

        Iterator<Integer> it = adjListArray[source].listIterator();
        while(it.hasNext()) {
            int next = it.next();
            if(!visited[next]) {
                DFSHelper(next, visited);
            }

        }
    }
}
