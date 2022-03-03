package ListOfDepths;

import Tree.BinaryTree;

import java.util.ArrayList;
import java.util.LinkedList;

public class ListOfDepths {
    public static void main(String[] args) {
        BinaryTree<String> bt = new BinaryTree<>("0");
        BinaryTree<String> btleft = new BinaryTree<>("00");
        BinaryTree<String> btleftleft = new BinaryTree<>("000");

        BinaryTree<String> btright = new BinaryTree<>("01");
        BinaryTree<String> btrightleft = new BinaryTree<>("010");
        BinaryTree<String> btrightleftleft = new BinaryTree<>("0100");
        BinaryTree<String> btrightleftleftleft = new BinaryTree<>("01000");
        BinaryTree<String> btrightleftleftleftleft = new BinaryTree<>("010000");

        bt.left = btleft;
        btleft.left = btleftleft;
        bt.right = btright;
        btright.left = btrightleft;
        btrightleft.left = btrightleftleft;
        btrightleftleft.left = btrightleftleftleft;
        btrightleftleftleft.left = btrightleftleftleftleft;

        System.out.println("Length of branches: " + lengthOfBranches(bt));

        System.out.println("List of depths: " + listOfDepths(bt));

        System.out.println("List of all branches: " + listOfAll(bt));
    }

    public static ArrayList<LinkedList> listOfDepths(BinaryTree bt) {
        ArrayList<LinkedList> ll = new ArrayList<>();
        lodHelper(bt, ll, 0);
        return ll;
    }

    public static void lodHelper(BinaryTree bt, ArrayList<LinkedList> ll, int depth) {
        if(bt == null) {
            return;
        }

        if(ll.size() == depth) {
            LinkedList newList = new LinkedList<>();
            newList.add(bt.data);
            ll.add(newList);
        }
        else {
            ll.get(depth).add(bt.data);
        }

        lodHelper(bt.right, ll, depth + 1);
        lodHelper(bt.left, ll, depth + 1);
    }

    public static LinkedList<Integer> lengthOfBranches(BinaryTree bt) {
        LinkedList<Integer> list = new LinkedList<>();
        lobHelper(bt, list, 0);
        return list;
    }

    public static void lobHelper(BinaryTree<String> bt, LinkedList all, int count) {
        if(bt.right == null && bt.left == null) {
            all.add(count);
        }
        else if(bt.right == null && bt.left != null) {
            lobHelper(bt.left, all, count + 1);
        }
        else if(bt.right != null && bt.left == null) {
            lobHelper(bt.right, all, count + 1);
        }
        else {
            lobHelper(bt.left, all, count + 1);
            lobHelper(bt.right, all, count + 1);
        }
    }

    public static LinkedList<LinkedList<Integer>> listOfAll(BinaryTree bt) {
        LinkedList<LinkedList<Integer>> ll = new LinkedList<>();
        loaHelper(bt, ll, new LinkedList());
        return ll;
    }
    public static void loaHelper(BinaryTree<String> bt, LinkedList all, LinkedList curr) {
        LinkedList<String> newList = new LinkedList<>(curr);
        newList.add(bt.data);
        if(bt.right == null && bt.left == null) {
            all.add(newList);
            return;
        }
        else if(bt.right == null && bt.left != null) {
            loaHelper(bt.left, all, newList);
        }
        else if(bt.right != null && bt.left == null) {
            loaHelper(bt.right, all, newList);
        }
        else {
            loaHelper(bt.left, all, newList);
            loaHelper(bt.right, all, newList);
        }
    }
}
