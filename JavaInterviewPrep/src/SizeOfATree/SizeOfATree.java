package SizeOfATree;

class TreeNode {
    public TreeNode(int data) {
        this.data = data;
    }
    TreeNode right, left;
    int data;
}
public class SizeOfATree {
    public static void main(String[] args) {

        TreeNode root = new TreeNode(0);

        TreeNode left = new TreeNode(1);

        TreeNode leftleft = new TreeNode(3);
        TreeNode leftright = new TreeNode(4);
        left.left = leftleft;
        left.right= leftright;

        TreeNode right = new TreeNode(2);

        TreeNode rightleft = new TreeNode(5);
        TreeNode rightright = new TreeNode(6);
        right.left = rightleft;
        right.right = rightright;

        root.right = right;
        root.left = left;

        System.out.println("Result: " + sizeOfTree(root));
    }

    public static int sizeOfTree(TreeNode current) {
        if(current == null) {
            return 0;
        }

        return sizeOfTree(current.left) + sizeOfTree(current.right) + 1;
    }
}
