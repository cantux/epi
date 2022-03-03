package LinkedList;

public class LL<T> {

    public Node<T> head = null;
    public LL() { }

    public void add(T value) {
        if(head == null)
        {
            head = new Node(value);
        }
        else
        {
            Node next = head;
            while(next.next != null)
            {
                next = next.next;
            }

            next.next = new Node(value);
        }
    }

    public void printList() {
        Node<T> next = head;
        int i = 0;
        while(next != null) {
            System.out.println("item: " + i + " is: " + next.toString());
            i++;
            next = next.next;
        }
    }


    public Node reverseList(Node curr, Node prev) {
        if (curr.next == null) {
            head = curr;

            /* Update next to prev node */
            curr.next = prev;

            return head;
        }

        /* Save curr->next node for recursive call */
        Node next1 = curr.next;

        /* and update next ..*/
        curr.next = prev;

        reverseList(next1, curr);
        return head;
    }
}
