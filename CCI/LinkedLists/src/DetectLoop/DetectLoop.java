package DetectLoop;

import LinkedList.Node;

import java.util.HashSet;

public class DetectLoop {
    public static void main(String[] args) {
        Node<Integer> list = new Node<>(0);
        list.next = new Node<>(1);

        Node<Integer> nodeLoopStart = new Node<>(2);
        list.next.next = nodeLoopStart;

        nodeLoopStart.next = new Node(3);
        nodeLoopStart.next.next = new Node(4);
        nodeLoopStart.next.next.next = nodeLoopStart;
    }

    // Function that detects loop in the list
    public static int detectAndRemoveLoop(Node node) {
        Node slow = node, fast = node;
        while (slow != null && fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            // If slow and fast meet at same point then loop is present
            if (slow == fast) {
                removeLoop(slow, node);
                return 1;
            }
        }
        return 0;
    }

    // Function to remove loop
    public static void removeLoop(Node loop, Node curr) {
        Node ptr1 = null, ptr2 = null;

        /* Set a pointer to the beging of the Linked List and
         move it one by one to find the first node which is
         part of the Linked List */
        ptr1 = curr;
        while (1 == 1) {

            /* Now start a pointer from loop_node and check if it ever
             reaches ptr2 */
            ptr2 = loop;
            while (ptr2.next != loop && ptr2.next != ptr1) {
                ptr2 = ptr2.next;
            }

            /* If ptr2 reahced ptr1 then there is a loop. So break the
             loop */
            if (ptr2.next == ptr1) {
                break;
            }

            /* If ptr2 did't reach ptr1 then try the next node after ptr1 */
            ptr1 = ptr1.next;
        }

        /* After the end of loop ptr2 is the last node of the loop. So
         make next of ptr2 as NULL */
        ptr2.next = null;
    }
}
