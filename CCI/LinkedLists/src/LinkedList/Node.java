package LinkedList;

public class Node<T> {
    public Node next = null, prev = null, last = null;
    public T data;

    public Node(T data) {
        last = this;
        this.data = data;
    }

    public void appendToTail(T data) {
        Node<T> newNode = new Node(data);
        last.next = newNode;
        newNode.prev = last;
        last = newNode;
    }

    public String toString() {
        Node current = this;
        String toString = "";
        while(current != null) {
            toString += current.data.toString();
            current = current.next;
        }
        return toString;
    }
}