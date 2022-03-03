package TreeNode.BTPathSum;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class BTPathSum {
    public static void main(String[] args) {
        TreeNode bt = new TreeNode(1);
        TreeNode btleft = new TreeNode(2);
        TreeNode btright = new TreeNode(3);

        TreeNode btleftleft = new TreeNode(4);
        TreeNode btleftright = new TreeNode(5);

        TreeNode btrightleft = new TreeNode(6);
        TreeNode btrightright = new TreeNode(7);

        bt.left = btleft;
        bt.right = btright;

        btleft.left = btleftleft;
        btleft.right = btleftright;

        btright.left = btrightleft;
        btright.right = btrightright;

        System.out.println("result1: " + pathSum(bt, 7));
        System.out.println("result1: " + pathSum(bt, 8));
        System.out.println("result1: " + pathSum(bt, 9));
        System.out.println("result1: " + pathSum(bt, 10));
        System.out.println("result1: " + pathSum(bt, 11));
    }

    public static List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> list = new ArrayList();
        if(root != null) helper(root, 0, sum, new ArrayList(), list);
        return list;
    }

    public static void helper(TreeNode current, int sumSoFar, int sum, List<Integer> listSoFar, List<List<Integer>> list) {
        if(current == null) {
            return;
        }

        listSoFar.add(current.val);
        int currentSum = sumSoFar + current.val;
        if(current.left == null && current.right == null && currentSum == sum) {
            list.add(new LinkedList<>(listSoFar));
//            listSoFar.remove(listSoFar.size() - 1);
//            return;
        }

        helper(current.left, currentSum, sum, listSoFar, list);
        helper(current.right, currentSum, sum, listSoFar, list);
        listSoFar.remove(listSoFar.size() - 1);
    }
}
