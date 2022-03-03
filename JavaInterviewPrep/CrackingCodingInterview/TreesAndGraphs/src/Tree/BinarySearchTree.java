package Tree;

public class BinarySearchTree {
    public int data;
    public BinarySearchTree left, right;

    public BinarySearchTree(int data) {
        this.data = data;
    }

    public void insertInorder(int data) {
        if(this.data < data) {
            if(left == null) {
                left = new BinarySearchTree(data);
            }
            else {
                left.insertInorder(data);
            }
        }
        else {
            if(right== null) {
                right = new BinarySearchTree(data);
            }
            else {
                right.insertInorder(data);
            }
        }
    }

    public BinarySearchTree find(int d) {
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
