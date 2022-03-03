package DeleteMiddleNode;

import LinkedList.Node;

public class DeleteMiddleNode {
    public static void main(String[] args) {
        Node<Integer> list = new Node(0);
        Node current = list;

        Node test = null;

        for(int i = 1; i < 10; i++) {
            Node<Integer> new_node = new Node(i);
            if(i == 5) {
                test = current;
            }
            current.next = new_node;
            current = new_node;
        }

        System.out.println("list is: " + list);

        deleteMiddle(test);

        System.out.println("list is: " + list);
    }

    public static void deleteMiddle(Node node)
    {
        Node nextItem = node.next;
        node.next = nextItem.next;
        node.data = nextItem.data;
    }
}
