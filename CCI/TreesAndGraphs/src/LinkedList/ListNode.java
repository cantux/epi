package LinkedList;

public class ListNode<T> {
    public ListNode next = null, prev = null, last = null;
    public T data;

    public ListNode(T data) {
        this.data = data;
    }

    public void appendToTail(T data) {
        ListNode<T> newNode = new ListNode(data);
        if(last != null) {
            last.next = newNode;
        }
        newNode.prev = last;
        last = newNode;
    }

    public String toString() {
        ListNode current = this;
        String toString = "";
        while(current.next != null) {
            toString += current.data.toString();
            current = current.next;
        }
        return toString;
    }

}
