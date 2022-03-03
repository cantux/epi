package RandomNode;

import java.util.Random;

public class RandomNode {
    public static void main(String[] args) {

    }

    class Tree {
        TreeNode root = null;

        public int size() { return root == null ? 0: root.size; }

        public TreeNode getRandomNode() {
            if(root == null) return null;

            Random random = new Random();
            int i = random.nextInt(size());
            return root.getIthNode(i);
        }

        public void insertInorder(int value) {
            if (root == null) {
                root = new TreeNode(value);
            }
            else {
                root.insertInorder(value);
            }
        }
    }

    class TreeNode {
        public int data, size;
        public TreeNode left, right;

        public TreeNode(int data) {
            this.data = data;
            size = 1;
        }

        public TreeNode getIthNode(int i) {
            int leftSize = left == null? 0: left.size;
            if(i < leftSize) {
                return left.getIthNode(i);
            }
            else if(i == leftSize) {
                return this;
            }
            else {
                return right.getIthNode(i - leftSize  + 1);
            }
        }

        public TreeNode getRandomNode() {
            int leftSize = left ==  null ? 0: left.size;
            Random random = new Random();
            int index = random.nextInt(size);
            if(index < leftSize) {
                return left.getRandomNode();
            }
            else if(index == leftSize) {
                return this;
            }
            else{
                return right.getRandomNode();
            }
        }

        public void insertInorder(int data) {
            if(this.data < data) {
                if(left == null) {
                    left = new TreeNode(data);
                }
                else {
                    left.insertInorder(data);
                }
            }
            else {
                if(right== null) {
                    right = new TreeNode(data);
                }
                else {
                    right.insertInorder(data);
                }
            }
            size++;
        }

        public TreeNode find(int d) {
            if(d == data) {
                return this;
            }
            else if(d <= data) {
                return left != null ? left.find(d): null;
            }
            else if(d > data) {
                return right != null ? right.find(d) : null;
            }
            return null;
        }
    }
}
