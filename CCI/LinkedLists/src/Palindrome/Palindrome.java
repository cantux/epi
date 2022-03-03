package Palindrome;

import LinkedList.LL;
import LinkedList.Node;

public class Palindrome {
    public static void main(String[] args) {
        LL<String> list0 = new LL();
        list0.head = new Node("a");
        list0.head.next = new Node("a");
        list0.head.next.next = new Node("c");

        LL<String> list1 = new LL();
        list1.head = new Node("a");
        list1.head.next = new Node("a");
        list1.head.next.next = new Node("a");

        LL<String> list2 = new LL();
        list2.head = new Node("1");
        list2.head.next = new Node("2");
        list2.head.next.next = new Node("3");

//        System.out.println("result: " + reverseList(list2));
        System.out.println("result: " + checkPalindrome(list0));
        System.out.println("result: " + checkPalindrome(list1));
        System.out.println("result: " + checkPalindrome(list2));
    }

    public static boolean checkPalindrome(LL list) {
        Node z = reverseList(list, list.head, null);

        System.out.println("reversed list is: " + z);

        return true;
    }

    public static Node reverseList(LL list, Node curr, Node prev) {
        if (curr.next == null) {
            list.head = curr;

            /* Update next to prev node */
            curr.next = prev;

            return list.head;
        }

        /* Save curr->next node for recursive call */
        Node next1 = curr.next;

        /* and update next ..*/
        curr.next = prev;

        reverseList(list, next1, curr);
        return list.head;
    }


}
