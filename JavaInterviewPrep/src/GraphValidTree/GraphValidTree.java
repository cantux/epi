package GraphValidTree;

public class GraphValidTree {

    public boolean validTree(int n, int[][] edges) {
        int[] connection = new int[n];
        for (int i = 0; i < n; i++) connection[i] = i;

        for (int i = 0; i < edges.length; i++) {
            int xRoot = find(connection, edges[i][0]);
            int yRoot = find(connection, edges[i][1]);

            if(xRoot == yRoot) return false;

            union(connection, xRoot, yRoot);
        }

        return edges.length == n - 1;
    }

    private int find(int[] connection, int x){
        while(x != connection[x]) {
            x = connection[x];
        }
        return x;
    }

    private void union(int[] connection, int x, int y) {
        int xRoot = find(connection, x);
        int yRoot = find(connection, y);
        if(xRoot == yRoot) return;

        connection[xRoot] = yRoot;
    }
}
