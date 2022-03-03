package MergeTwoSortedLists;

public class MergeTwoSortedLists {

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(4);

        ListNode l2 = new ListNode(1);
        l2.next = new ListNode(3);
        l2.next.next = new ListNode(4);

        ListNode newL = mergeTwoLists(l1, l2);
        int i = 0;
         while(newL != null) {
             System.out.println("i: " + i + " is: " + newL.val);
             newL = newL.next;
             i++;
         }

    }
    public static ListNode mergeTwoLists2(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode curr = result;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        if (l1 != null) {
            curr.next = l1;
        }
        if (l2 != null) {
            curr.next = l2;
        }
        return result.next;
    }

    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode first = l1;
        ListNode second = l2;
        ListNode curr = head;
        while(first != null && second != null) {
            int currVal;
            if(first.val < second.val) {
                currVal = first.val;
                first = first.next;
            }
            else {
                currVal = second.val;
                second = second.next;
            }

            curr.next = new ListNode(currVal);
            curr = curr.next;
        }

        if(first == null) {
            curr.next = second;
        }
        else {
            curr.next = first;
        }
        return head.next;
    }
}
