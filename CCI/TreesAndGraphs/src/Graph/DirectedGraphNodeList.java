package Graph;

import LinkedList.ListNode;

public class DirectedGraphNodeList<T> {
    public T data;
    public boolean visited = false;
    public ListNode<DirectedGraphNodeList<T>> children = null;

    public DirectedGraphNodeList(T data) {
        this.data = data;
    }

    public void addChild(T childData) {
        if(children == null) {
            children = new ListNode(new DirectedGraphNodeList(childData));
        }
        else {
            children.appendToTail(new DirectedGraphNodeList(childData));
        }
    }

    public void appendChild(DirectedGraphNodeList<T> child) {
        if(children == null) {
            children = new ListNode(child);
        }
        else {
            children.appendToTail(child);
        }
    }

    public String toString() {
        return String.valueOf(data);
    }

}
