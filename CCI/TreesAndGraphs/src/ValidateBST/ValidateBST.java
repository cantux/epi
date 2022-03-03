package ValidateBST;

import Tree.BinaryTree;

public class ValidateBST {
    public static void main(String[] args) {
        BinaryTree<Integer> bt = new BinaryTree<>(5);
        BinaryTree<Integer> btleft = new BinaryTree<>(3);
        BinaryTree<Integer> btleftleft = new BinaryTree<>(2);

        BinaryTree<Integer> btright = new BinaryTree<>(10);
        BinaryTree<Integer> btrightleft = new BinaryTree<>(9);
        BinaryTree<Integer> btrightleftleft = new BinaryTree<>(4);
//        BinaryTree<Integer> btrightleftleftleft = new BinaryTree<>(7);
//        BinaryTree<Integer> btrightleftleftleftleft = new BinaryTree<>(4);

        bt.left = btleft;
        btleft.left = btleftleft;
        bt.right = btright;
        btright.left = btrightleft;
        btrightleft.left = btrightleftleft;
//        btrightleftleft.left = btrightleftleftleft;
//        btrightleftleftleft.left = btrightleftleftleftleft;


        System.out.println("validate BST right: " + validateBSTMinMax(btright));
        System.out.println("validate BST: " + validateBSTMinMax(bt));

        System.out.println("validate BST right: " + validateBSTStaticVar(btright));
        System.out.println("validate BST: " + validateBSTStaticVar(bt));

    }

    public static boolean validateBSTMinMax(BinaryTree curr) {
        return validateBSTMinMaxHelper(curr, null, null);
    }

    public static boolean validateBSTMinMaxHelper(BinaryTree<Integer> curr, Integer min, Integer max) {
        if(curr == null) return true;

        if((min != null && min > curr.data) || (max != null && max < curr.data)) {
            return false;
        }
        if(!validateBSTMinMaxHelper(curr.left, min, curr.data) || !validateBSTMinMaxHelper(curr.right, curr.data, max)) {
            return false;
        }
        return true;
    }

    // This works cuz inorder traversal of BST is sorted.
    static Integer last = null;
    public static boolean validateBSTStaticVar(BinaryTree<Integer> bt) {
        if(bt == null) return true;

        if(!validateBSTStaticVar(bt.left)) return false;

        if(last != null && bt.data <= last) {
            return false;
        }
        last = bt.data;

        if(!validateBSTStaticVar(bt.right)) return false;

        return true;
    }
//
//    public static boolean validateNothing(BinaryTree<Integer> curr) {
//        if(curr == null) return true;
//
//        boolean leftCorrect = true, rightCorrect = true;
//        if(curr.left != null) {
//            leftCorrect = validateNothing(curr.left) && curr.data > curr.left.data;
//        }
//        if(curr.right != null) {
//            rightCorrect = validateNothing(curr.right) && curr.data <= curr.right.data;
//        }
//        return leftCorrect && rightCorrect;
//    }
}
