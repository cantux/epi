package ReturnKthLast;

import LinkedList.Node;

public class ReturnKthLast {
    public static void main(String[] args) {
        Node<Integer> list = new Node(0);
        for (int i = 1; i < 10; i++) {
            list.appendToTail(i);
        }

//        System.out.println("item on 6th pos is: " + returnKthLast(list, 4));
//        System.out.println("item on 6th pos is: " + recGetKth(list, 4));
//
        Integer val = new Integer(0);
        retrunKthToTheLast(list, 3, val);
        System.out.println("resilt: " + val);
    }

    public static int retrunKthToTheLast(Node<Integer> list, int k, Integer value) {
        if(list == null) {
            return 0;
        }

        int count = retrunKthToTheLast(list.next, k, value) + 1;

        if(k == count) {
            System.out.println("value: " + list.data);
            value = list.data;
        }

        return count;
    }
}
