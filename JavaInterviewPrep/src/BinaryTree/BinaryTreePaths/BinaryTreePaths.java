package BinaryTree.BinaryTreePaths;

import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class BinaryTreePaths {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> list = new ArrayList();
        if(root != null) helper(root, "", list);
        return list;
    }

    public void helper(TreeNode current, String soFar, List<String> list) {
        if(current.left == null && current.right == null) {
            list.add(soFar + current.val);
            return ;
        }

        if(current.left != null) helper(current.left, soFar + current.val + "->", list);
        if(current.right != null) helper(current.right, soFar + current.val + "->", list);
    }
}
