package Tree;

public class BinaryTreeWithParent<T> {

    public T data;

    public BinaryTreeWithParent<T> parent, left, right;

    public BinaryTreeWithParent(T data) {
        this.data = data;
    }
}
