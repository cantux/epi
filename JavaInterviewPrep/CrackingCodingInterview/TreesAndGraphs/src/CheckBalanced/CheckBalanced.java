package CheckBalanced;

import Tree.BinaryTree;

public class CheckBalanced {
    public static void main(String[] args) {
        BinaryTree<String> bt = new BinaryTree<>("0");
        BinaryTree<String> btleft = new BinaryTree<>("00");
        BinaryTree<String> btright = new BinaryTree<>("01");

        BinaryTree<String> btleftleft = new BinaryTree<>("000");
        BinaryTree<String> btleftright = new BinaryTree<>("001");

        BinaryTree<String> btrightleft = new BinaryTree<>("010");
        BinaryTree<String> btrightright = new BinaryTree<>("011");

        BinaryTree<String> btrightrightright = new BinaryTree<>("0111");
        BinaryTree<String> btrightrightrightright = new BinaryTree<>("01111");

        bt.left = btleft;
        bt.right = btright;

        btleft.left = btleftleft;
        btleft.right = btleftright;

        btright.left = btrightleft;
        btright.right = btrightright;

        btrightright.right = btrightrightright;

        bt.prettyPrintBalancedTree();

        System.out.println("result checkBalanced: " + checkBalanced(bt));

        btrightrightright.right = btrightrightrightright;
        System.out.println("result after unbalance: " + checkBalanced(bt));
    }

    // uses the tactic of bubbling up the error
    public static boolean checkBalanced(BinaryTree bt) {
        return checkBalancedHelper(bt) != Integer.MAX_VALUE;
    }

    public static int checkBalancedHelper(BinaryTree curr) {
        if(curr == null) {
            return 0;
        }

        int left = 0, right = 0;
        if(curr.left != null) {
            left = checkBalancedHelper(curr.left);
        }
        if(curr.right != null) {
            right = checkBalancedHelper(curr.right);
        }

        if(Math.abs(left - right) > 1) {
            return Integer.MAX_VALUE;
        }
        return Math.max(left, right) + 1;
    }
}
