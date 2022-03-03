package LinkedList;

public class LinkedListTest {
    public static void main(String[] args) {
        LL list = new LL();

        for(int i = 0; i < 10; i++) {
            list.add(i);
        }
        list.printList();

    }
}
