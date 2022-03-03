package KthSmallestIn2DArr;

import java.util.Comparator;
import java.util.PriorityQueue;

class Node {
    public int val, col, row;
    public String toString() {
        return "val: " + val + " col: " + col + " row: " + row;
    }
}

public class KthSmallestIn2dArr {
    public static void main(String[] args) {
        int[][] arr = new int[][] {
                {10, 20, 30, 40},
                {15, 25, 31, 45},
                {25, 29, 32, 48},
                {32, 33, 39, 50},
        };
        System.out.println("result is: " + kthSmallest(arr, 7));
    }

    public static int kthSmallest(int[][] arr, int k) {
        if(arr.length == 0) {
            return -1;
        }

        PriorityQueue<Node> pq = new PriorityQueue<>(new Comparator<Node>() {
            public int compare(Node n1, Node n2) {
                return n1.val - n2.val;
            }
        });

        for(int i = 0; i < arr.length; i++) {
            Node n = new Node();
            n.val = arr[0][i];
            n.col = i;
            n.row = 0;
            pq.add(n);
        }

        Node node = null;
        for(int i=0; i < k; i++) {
            node = pq.poll();
            if(node.row < arr.length - 1) {
                Node newNode = new Node();

                newNode.val = arr[node.row +1][node.col];
                newNode.row = node.row + 1;
                newNode.col = node.col;

                pq.add(newNode);
            }
        }

        return node.val;
    }
}
