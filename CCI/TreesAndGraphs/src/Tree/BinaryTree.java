package Tree;

import CheckBalanced.CheckBalanced;
import ListOfDepths.ListOfDepths;

import java.util.*;
import java.util.stream.IntStream;

public class BinaryTree<T> {

    public static void main(String[] args) {
        BinaryTree<Integer> t0 = new BinaryTree<>(20);

        BinaryTree<Integer> t1 = new BinaryTree<>(10);
        BinaryTree<Integer> t2 = new BinaryTree<>(15);
        BinaryTree<Integer> t3 = new BinaryTree<>(5);

        BinaryTree<Integer> t4 = new BinaryTree<>(30);
        BinaryTree<Integer> t5 = new BinaryTree<>(35);
        BinaryTree<Integer> t6 = new BinaryTree<>(25);

        t0.left = t1;
        t1.left = t3;
        t1.right = t2;

        t0.right = t4;
        t4.left = t6;
        t4.right = t5;

        t0.prettyPrintBalancedTree();

    }
    public T data;
    public BinaryTree<T> left, right;

    public BinaryTree(T data) {
        this.data = data;
    }

    // if the tree is balanced pretty print
    public void prettyPrintBalancedTree() {
//        if(CheckBalanced.checkBalanced(this)){
            LinkedList<Integer> depths = ListOfDepths.lengthOfBranches(this);
            Optional<Integer> maxDepth = depths.stream().reduce((x, y) -> Math.max(x,y));
            if(maxDepth.isPresent()) {
                Queue q = new LinkedList();
                ((LinkedList) q).addFirst(this);
                prettyPrintHelper(q, 0, maxDepth.get(), 2);
            }
            else System.out.println("Java 8 reduce returns maybe");

//        }
//        else {
//            System.out.println("tree is not balanced luv");
//        }
    }

    private ArrayList<T> toArray() {
        Queue q = new LinkedList();
        ArrayList<T> linear = new ArrayList();
        BinaryTree curr = this;
        ((LinkedList) q).addFirst(curr);
        while(q.size() != 0) {
            linear.add((T) q.poll());
            if(curr.left != null) {
                ((LinkedList) q).addFirst(curr.left);
            }
            if(curr.right != null) {
                ((LinkedList) q).addFirst(curr.right);
            }
        }
        return linear;
    }

    private void prettyPrintHelper(Queue q, int height, int max, int unit) {
        if(q.isEmpty()) return;

        Queue leaves = new LinkedList();

        while(q.size() != 0)
        {
            BinaryTree next = (BinaryTree) q.poll();

            if(next != null)
            {
                repeat((int)(unit * Math.pow(2.0, max - height + 1)), () -> System.out.print(" "));
                System.out.print(next.data);

                ((LinkedList) leaves).addFirst(next.left);
                ((LinkedList) leaves).addFirst(next.right);
            }
        }

        System.out.println();

        prettyPrintHelper(leaves,height + 1, max, unit);
    }

    private void repeat(int count, Runnable action) {
        IntStream.range(0, count).forEach(i -> action.run());
    }

    public static BinaryTree<Integer> buildBSTFromArray(int[] arr) {
        return fromArray(arr, 0, arr.length);
    }

    public static BinaryTree<Integer> fromArray(int[] arr, int min, int max) {
        if(min>max) {
            return null;
        }

        int mid = (min + max) / 2;
        BinaryTree<Integer> root = new BinaryTree<>(arr[mid]);
        root.left = fromArray(arr, min, mid - 1);
        root.right = fromArray(arr, mid + 1, max);

        return root;
    }

    public static void invert(BinaryTree bt) {
        if(bt == null) {
            return;
        }

        BinaryTree temp = bt.left;
        bt.left = bt.right;
        bt.right = temp;
        invert(bt.left);
        invert(bt.right);
    }

    public static void leftView(BinaryTree root) {
        int[] level = { 0 };
        leftView(root, level, 1);
    }

    public static void leftView(BinaryTree root, int[] level, int maxLevel) {
        if(root == null) {
            return;
        }

        if(level[0] < maxLevel) {
            System.out.println(root.data);
            level[0] = maxLevel;
        }

        leftView(root.left, level, maxLevel + 1);
        leftView(root.right, level, maxLevel + 1);
    }
}
