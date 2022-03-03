package SumLists;

import LinkedList.Node;

/**
 * You have two numbers represented by a linked list where each node contains a single digit
 * The digits are stored in reverse order, such that the 1's digit is at the head of the list.
 * Write a function that adds the two numbers and returns the sum asa linked list.
 *
 * Follow up: suppose the digits are stored in forward order
 */
public class SumLists {
    public static void main(String[] args) {
        Node<Double> list0 = new Node(9.0);

        list0.next = new Node(5.0);

        Node<Double> list1 = new Node(9.0);
        list1.next = new Node(9.0);
        list1.next.next = new Node(1.0);

        System.out.println("result: " + sumLists(list0, list1));



//        Node<Double> list0 = new Node(9.0);
//
//        list0.next = new Node(5.0);
//
//        Node<Double> list1 = new Node(9.0);
//        list1.next = new Node(9.0);
//        list1.next.next = new Node(1.0);
//
//        System.out.println("result: " + sumLists(list0, list1));
    }

    public static double sumLists(Node<Double> list1, Node<Double> list2) {
        int digit = 0;
        double sum = 0;
        while(list1 != null && list2 != null) {

            double list1Value = list1.data * Math.pow(10, digit);
            double list2Value = list2.data * Math.pow(10, digit);

            sum += list1Value + list2Value;

            digit++;

            list1 = list1.next;
            list2 = list2.next;
        }

        int tempDigit = digit;
        if(list1 != null) {
            while(list1 != null) {
                sum += list1.data * Math.pow(10, tempDigit++);
                list1= list1.next;
            }
        }

        if(list2 != null) {
            while(list2 != null) {
                sum += list2.data * Math.pow(10, digit++);
                list2 = list2.next;
            }
        }

        return sum;
    }
}
