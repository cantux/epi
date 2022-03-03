package InorderSuccessor;

import Tree.BinaryTreeWithParent;

import java.util.HashMap;

public class InorderSuccessor {
    public static void main(String[] args) {

        HashMap<Integer, Integer> hm = new HashMap<>();

        hm.put(20 ,4);
        hm.put(10 ,2);

        hm.put(15 ,3);
        hm.put(5 ,1);

        hm.put(30 ,6);
        hm.put(25 ,5);
        hm.put(35 ,7);

        BinaryTreeWithParent<Integer> t0 = new BinaryTreeWithParent<>(20);

        BinaryTreeWithParent<Integer> t1 = new BinaryTreeWithParent<>(10);
        BinaryTreeWithParent<Integer> t2 = new BinaryTreeWithParent<>(15);
        BinaryTreeWithParent<Integer> t3 = new BinaryTreeWithParent<>(5);

        BinaryTreeWithParent<Integer> t4 = new BinaryTreeWithParent<>(30);
        BinaryTreeWithParent<Integer> t5 = new BinaryTreeWithParent<>(35);
        BinaryTreeWithParent<Integer> t6 = new BinaryTreeWithParent<>(25);

        t0.left = t1;
        t1.left = t3;
        t1.right = t2;

        t0.right = t4;
        t4.left = t6;
        t4.right = t5;

        System.out.println("successor of: " + hm.get(t0.data) + " is: " + hm.get(successor(t0).data));
        System.out.println("successor of: " + hm.get(t1.data) + " is: " + hm.get(successor(t1).data));
        System.out.println("successor of: " + hm.get(t2.data) + " is: " + hm.get(successor(t2).data));
        System.out.println("successor of: " + hm.get(t3.data) + " is: " + hm.get(successor(t3).data));
        System.out.println("successor of: " + hm.get(t4.data) + " is: " + hm.get(successor(t4).data));
        System.out.println("successor of: " + hm.get(t5.data) + " is: " + hm.get(successor(t5).data));

    }

    public static BinaryTreeWithParent successor(BinaryTreeWithParent<Integer> bt) {
        if(bt == null) {
            return null;
        }
        else if(bt.right != null) {
            return leftMostChild(bt.right);
        }
        else {
            BinaryTreeWithParent<Integer> curr = bt;
            BinaryTreeWithParent<Integer> parent = bt.parent;
            while(parent != null && parent.left != curr) {
                curr = parent;
                parent = parent.parent;
            }
            return parent;
        }
    }

    public static BinaryTreeWithParent leftMostChild(BinaryTreeWithParent<Integer> n ){
        if(n == null) {
            return null;
        }
        while(n.left != null) {
            n = n.left;
        }
        return n;
    }
}
