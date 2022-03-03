package Intersection;

import LinkedList.LL;
import LinkedList.Node;

public class Intersection {
    public static void main(String[] args) {
        LL<String> list0 = new LL();
        list0.head = new Node("a");
        list0.head.next = new Node("a");
        list0.head.next.next = new Node("c");

        LL<String> list1 = new LL();
        list1.head = new Node("a");
        list1.head.next = new Node("a");
        list1.head.next.next = list0.head;

        LL<String> list2 = new LL();
        list2.head = new Node("1");
        list2.head.next = list0.head;

        System.out.println("result is: " + getIntersection(list1, list2));
    }

    static Node getIntersection(LL list1, LL list2) {
        Node l1_head = list1.reverseList(list1.head, null);
        Node l2_head = list2.reverseList(list2.head, null);

        while(l1_head.next != null && l2_head.next != null) {
            if(l1_head.next != l2_head.next) {
                return l1_head;
            }
        }
        return null;
    }
}
