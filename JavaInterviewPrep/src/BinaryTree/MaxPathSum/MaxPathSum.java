package BinaryTree.MaxPathSum;

class Node {

    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = right = null;
    }
}

// An object of Res is passed around so that the
// same value can be used by multiple recursive calls.
class Res {
    public int val;
}

class BinaryTree {

    // Root of the Binary Tree
    Node root;

    // This function returns overall maximum path sum in 'res'
    // And returns max path sum going through root.
    int findMaxUtil(Node node, Res res)
    {

        // Base Case
        if (node == null)
            return 0;

        int l = findMaxUtil(node.left, res);
        int r = findMaxUtil(node.right, res);

        // check if any child sums is worth considering
        // if so, add it to the path, otherwise ignore them
        int maxSingleBranchSum = Math.max(Math.max(l, r) + node.data,
                node.data);

        // find the sum of both leaves
        // if it's bigger than only considering a single branch
        int bothBranchSum = Math.max(maxSingleBranchSum, l + r + node.data);

        // save the maximum subsum we found so far
        res.val = Math.max(res.val, bothBranchSum);

        // always propogate the largest branch sum(don't propagate )
        return maxSingleBranchSum;
    }

    int findMaxSum() {
        return findMaxSum(root);
    }

    // Returns maximum path sum in tree with given root
    int findMaxSum(Node node) {

        // Initialize result
        // int res2 = Integer.MIN_VALUE;
        Res res = new Res();
        res.val = Integer.MIN_VALUE;

        // Compute and return result
        findMaxUtil(node, res);
        return res.val;
    }

    /* Driver program to test above functions */
    public static void main(String args[]) {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(10);
        tree.root.left = new Node(2);
        tree.root.right = new Node(10);
        tree.root.left.left = new Node(20);
        tree.root.left.right = new Node(1);
        tree.root.right.right = new Node(-25);
        tree.root.right.right.left = new Node(3);
        tree.root.right.right.right = new Node(4);
        System.out.println("maximum path sum is : " +
                tree.findMaxSum());
    }
}