package CommonAncestor;

import Tree.BinaryTree;

public class CommonAncestor {

    public static void main(String[] args) {

    }

    public static BinaryTree<Integer> commonAncestor(BinaryTree<Integer> root, BinaryTree<Integer> a, BinaryTree<Integer> b) {
        if(root == null) {
            return null;
        }

        boolean aIsOnLeft = covers(root.left, a);
        boolean bIsOnLeft = covers(root.left, b);

        if(aIsOnLeft != bIsOnLeft) { // Nodes are on different side
            return root;
        }

        BinaryTree<Integer> childSide = aIsOnLeft ? root.left : root.right;
        return commonAncestor(childSide, a, b);
    }

    public static boolean covers(BinaryTree<Integer> root, BinaryTree<Integer> p) {
        if(root == null) {
            return false;
        }

        if(root == p) {
            return true;
        }

        return covers(root.left, p) || covers(root.right, p);
    }

    BinaryTree<Integer> lca(BinaryTree<Integer> node, int n1, int n2)
    {
        if (node == null)
            return null;

        // If both n1 and n2 are smaller than root, then LCA lies in left
        if (node.data > n1 && node.data > n2)
            return lca(node.left, n1, n2);

        // If both n1 and n2 are greater than root, then LCA lies in right
        if (node.data < n1 && node.data < n2)
            return lca(node.right, n1, n2);

        return node;
    }
}
