package CloneGraph;

import java.util.*;

class UndirectedGraphNode {
    int label;
    List<UndirectedGraphNode> neighbors;
    UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
}

public class CloneGraph {

    public static void main(String[] args) {
        UndirectedGraphNode g0 = new UndirectedGraphNode(0);
        UndirectedGraphNode g1 = new UndirectedGraphNode(1);
        UndirectedGraphNode g2 = new UndirectedGraphNode(2);
        g0.neighbors.add(g1);
        g0.neighbors.add(g2);
        g1.neighbors.add(g2);

        UndirectedGraphNode g3 = new UndirectedGraphNode(3);
        UndirectedGraphNode g4 = new UndirectedGraphNode(4);
        g0.neighbors.add(g3);
        g1.neighbors.add(g4);

        UndirectedGraphNode g5 = new UndirectedGraphNode(5);
        g4.neighbors.add(g5);

        printDfs(g0);

        //printDfs(cloneGraph(g0));
        printDfs(clone2(g0));
    }

    static void printDfs(UndirectedGraphNode g) {
        Set<UndirectedGraphNode> set = new HashSet<>();
        set.add(g);
        printDfs(g, set);
    }

    static void printDfs(UndirectedGraphNode g, Set<UndirectedGraphNode> visited) {
        System.out.println(g.label);
        for(UndirectedGraphNode neighbor: g.neighbors) {
            if(!visited.contains(neighbor)) {
                visited.add(neighbor);
                printDfs(neighbor, visited);
            }
        }
    }

    public static UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;
        Map<UndirectedGraphNode,UndirectedGraphNode> map=new HashMap<>();
        dfs(map, node);
        return map.get(node);
    }
    private static void dfs(Map<UndirectedGraphNode,UndirectedGraphNode> map, UndirectedGraphNode curr){
        if(map.containsKey(curr)) return;
        map.put(curr, new UndirectedGraphNode(curr.label));
        for (UndirectedGraphNode next: curr.neighbors){
            dfs(map,next);
            map.get(curr).neighbors.add(map.get(next));
        }
    }

    public static UndirectedGraphNode clone2(UndirectedGraphNode node)
    {
        if(node == null) return null;
        Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();

        UndirectedGraphNode clone = new UndirectedGraphNode(node.label);
        map.put(node, clone);

        Queue<UndirectedGraphNode> q = new LinkedList<>();
        q.add(node);

        while(!q.isEmpty()) {
            UndirectedGraphNode curr = q.poll();
            UndirectedGraphNode cloneRef = map.get(curr);
            for(UndirectedGraphNode neighbor: curr.neighbors) {
                if(!map.containsKey(neighbor)) {
                    UndirectedGraphNode newNode = new UndirectedGraphNode(neighbor.label);
                    map.put(neighbor, newNode);
                    cloneRef.neighbors.add(newNode);
                    q.add(neighbor);
                }
            }
        }
        return clone;
    }
}
