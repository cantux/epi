package MyDisjointSet;

public class TreeDisjointSets {
    // nodes only know of their parents.

    class UnionFindNode {
        UnionFindNode parent;
        int value;
    }

    UnionFindNode[] sets;

    public TreeDisjointSets(int n) {
        sets = new UnionFindNode[n];
    }

    public union(int x, int y) {
        int xroot = find(x);
        int yroot = find(y);


    }

    // union by size
    // path compression


}
