package BinaryTree.DiameterOfBinaryTree;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class DiameterOfBinaryTree {

    int i = 1;
    public int diameterOfBinaryTree(TreeNode root) {
        maxLength(root);
        return i - 1;
    }

    public int maxLength(TreeNode root) {
        if(root == null) return 0;
        int leftMaxLength = maxLength(root.left);
        int rightMaxLength = maxLength(root.right);
        i = Math.max(i, rightMaxLength + leftMaxLength + 1);
        return Math.max(rightMaxLength, leftMaxLength) + 1;
    }


}