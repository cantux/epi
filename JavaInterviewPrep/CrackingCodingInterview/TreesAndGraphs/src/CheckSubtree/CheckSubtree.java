package CheckSubtree;

import Tree.BinaryTree;

/** T1 and T2 are two very large binary trees with T1 much bigger than T2.
 * Create an algorithm to determine if T2 is a subtree of T1
 */

public class CheckSubtree {
    public static void main(String[] args) {
        BinaryTree<String> bt = new BinaryTree<>("0");
        BinaryTree<String> btleft = new BinaryTree<>("00");
        BinaryTree<String> btright = new BinaryTree<>("01");

        BinaryTree<String> btleftleft = new BinaryTree<>("000");
        BinaryTree<String> btleftright = new BinaryTree<>("001");

        BinaryTree<String> btrightleft = new BinaryTree<>("010");
        BinaryTree<String> btrightright = new BinaryTree<>("011");

        bt.left = btleft;
        bt.right = btright;

        btleft.left = btleftleft;
        btleft.right = btleftright;

        btright.left = btrightleft;
        btright.right = btrightright;

        bt.prettyPrintBalancedTree();

        System.out.println("result checkSubTree: " + checkSubTree(bt, btleft));

        System.out.println("result checkSubTree: " + checkSubTree(btleft, btleftright));

        System.out.println("result checkSubTree: " + checkSubTree(bt, btleftright));
    }

    public static boolean checkSubTree(BinaryTree a, BinaryTree b) {
        if(a == null && b == null) {
            return true;
        }
        else if(a == null) {
            return false;
        }
        else if(a == b) {
            return checkSubTree(a.left, b.left) && checkSubTree(a.right, b.right);
        }
        return checkSubTree(a.left, b) || checkSubTree(a.right, b);
    }
}
