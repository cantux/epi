package Partition;

import LinkedList.Node;

/**
 * Write code to partition a linked list aroud a value x, such that all nodes less than x come before all nodes greater
 * than or equal to x. If x is contained within the list the values of x only need to be afther the elements less than x.
 * The partition element x can appear anywhere in the *right partition*, it does not need to appear between the
 * left and right partitions.
 */
public class Partition {
    public static void main(String[] args) {
        Node<Integer> list = new Node(0);
        Node current = list;

        for(int i = 1; i < 10; i++) {
            Node<Integer> new_node = new Node(10-i);
            current.next = new_node;
            current = new_node;
        }

        System.out.println("list is: " + list.next);

        System.out.println("list is: " + partition(list.next, 5));
    }

    public static Node<Integer> partition(Node<Integer> list, int value)
    {
        Node<Integer> smaller = new Node(0);
        Node<Integer> smallerHead = smaller;
        Node<Integer> larger = new Node(0);
        Node<Integer> largerHead = larger;
        while(list != null) {
            if(list.data < value) {
                smaller.next = new Node(list.data);
                smaller = smaller.next;
            }
            else {
                larger.next = new Node(list.data);
                larger = larger.next;
            }
            list = list.next;
        }
        System.out.println("larger: " + largerHead);
        System.out.println("smaller: " + smallerHead);
        if(smaller != null) {
            smaller.next = largerHead.next;
            return smallerHead.next;
        }
        return largerHead;
    }
}
