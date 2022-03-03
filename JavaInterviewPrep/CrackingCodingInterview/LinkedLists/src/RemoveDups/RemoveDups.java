package RemoveDups;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;

public class RemoveDups {

    public static void main(String[] args) {

        ArrayList allLists = new ArrayList<ArrayList<Integer>>();
        ArrayList list1 = new ArrayList<Integer>();
        ArrayList list2 = new ArrayList<Integer>();
        ArrayList list3 = new ArrayList<Integer>();
        ArrayList list4 = new ArrayList<Integer>();

        for(int i = 0; i < 10; i++) {
            list1.add(i);
            list2.add(i/2);
            list3.add(1);
            if(i % 2 == 0)
            {
                list4.add(0);
            }
            else
            {
                list4.add(1);
            }
        }

        allLists.add(list1);
        allLists.add(list2);
        allLists.add(list3);
        allLists.add(list4);

        Iterator it = allLists.iterator();
        while(it.hasNext())
        {
            ArrayList<Integer> list = (ArrayList<Integer>)it.next();
            System.out.println("test for a: " + list.toString() + " resluts to: ");
            printLinkedList(removeDuplicates(list));
        }
    }

    public static void printLinkedList(ArrayList list) {
        list.forEach((e) -> System.out.println("item: " + e));
    }

    public static ArrayList<Integer> removeDuplicates(ArrayList list) {
        HashSet encounters = new HashSet<Integer>();

        Iterator it = list.iterator();
        while (it.hasNext()) {
            int item = (int)it.next();
            if(encounters.contains(item))
            {
                it.remove();
            }
            else
            {
                encounters.add(item);
            }
        }

        return list;
    }

}
