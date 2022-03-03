package MergeKSorteLists;

import java.util.Comparator;
import java.util.PriorityQueue;

class MyPair {
    public ListNode node;
    public int listIndex;
    public MyPair(ListNode n, int li) {
        node = n;
        listIndex = li;
    }

    public String toString() { return "val is: " + node.val + " index is: " + listIndex; }
}

class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
}

public class MergeKSortedLists {
    public static void main(String[] args) {

        ListNode list1 = new ListNode(1);
        ListNode list2 = new ListNode(4);
        ListNode list3 = new ListNode(5);
        list1.next = list2;
        list2.next = list3;

        ListNode list4 = new ListNode(1);
        ListNode list5 = new ListNode(3);
        ListNode list6 = new ListNode(4);
        list4.next = list5;
        list5.next = list6;

        ListNode list7 = new ListNode(2);
        ListNode list8 = new ListNode(6);
        list7.next = list8;

        ListNode[] lists = new ListNode[] {
                list1,
                list4,
                list7
        };

        ListNode merged = mergeKLists(lists);

        while(merged!= null) {
            System.out.println("res: " + merged.val);
            merged = merged.next;
        }

    }

    public static ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0) return null;

        PriorityQueue<MyPair> pq = new PriorityQueue<MyPair>(lists.length, new Comparator<MyPair>() {
            public int compare(MyPair p1, MyPair p2) {
                return p1.node.val - p2.node.val;
            }
        });

        for(int i = 0; i < lists.length; i++) {
            if(lists[i] != null) {
                pq.offer(new MyPair(lists[i], i));
                lists[i] = lists[i].next;
            }
        }

        ListNode retList = new ListNode(0);
        ListNode curr = retList;
        while(!pq.isEmpty()) {
            MyPair p = pq.poll();

            curr.next = new ListNode(p.node.val);

            if(p.node.next != null && lists[p.listIndex] != null) {
                pq.offer(new MyPair(lists[p.listIndex], p.listIndex));
                lists[p.listIndex] = lists[p.listIndex].next;
            }

            curr = curr.next;
        }

        return retList.next;
    }
}
