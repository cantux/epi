package CopyListWithRandomPointer;

import java.util.HashMap;
import java.util.Map;

class RandomListNode {
    public int label;
    public RandomListNode next, random;
    RandomListNode(int x) { this.label = x; }

    public String toString() {
        return "label: " + label + " random: " + random.label;
    }
};
public class DeepCopyRandomPointerList {

    public static void main(String[] args) {
        RandomListNode rn0 = new RandomListNode(0);
        RandomListNode rn1 = new RandomListNode(1);
        RandomListNode rn2 = new RandomListNode(2);
        RandomListNode rn3 = new RandomListNode(3);
        RandomListNode rn4 = new RandomListNode(4);

        rn0.next = rn1;
        rn1.next = rn2;
        rn2.next = rn3;
        rn3.next = rn4;

        rn0.random = rn3;
        rn1.random = rn2;
        rn2.random = rn1;
        rn3.random = rn0;
        rn4.random = rn4;

//        RandomListNode curr = rn0;
//        while(curr != null) {
//            System.out.println(curr);
//            curr = curr.next;
//        }

        RandomListNode copied = copyRandomList(rn0);

        RandomListNode curr = copied;
        while(curr != null) {
            System.out.println(curr);
            curr = curr.next;
        }
    }

    public static RandomListNode copyRandomList(RandomListNode head) {

        RandomListNode retNode = new RandomListNode(-1);

        // keep a map of nodes to list of nodes
        //   old list  ------   new list node
        Map<RandomListNode, RandomListNode> randomMap = new HashMap();

        RandomListNode curr = head;
        RandomListNode currCopy = retNode;
        while(curr != null) {
            // deep copy contents expcept the random member var.
            RandomListNode copy = new RandomListNode(curr.label + 10);
            copy.random = curr.random;

            randomMap.put(curr, copy);

            currCopy.next = copy;
            currCopy = copy;

            curr = curr.next;
        }


        RandomListNode rn = retNode.next;
        while(rn != null) {
            rn.random = randomMap.get(rn.random);
            rn = rn.next;
        }

        return retNode.next;
    }
}
