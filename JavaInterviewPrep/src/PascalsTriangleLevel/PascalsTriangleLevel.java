package PascalsTriangleLevel;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class PascalsTriangleLevel {
    public static void main(String[] args) {
        System.out.println("result; " + getRow(0));
        System.out.println("result; " + getRow(1));
        System.out.println("result; " + getRow(2));
        System.out.println("result; " + getRow(3));
        System.out.println("result; " + getRow(4));
        System.out.println("result; " + getRow(5));
        System.out.println("result; " + getRow(6));
        System.out.println("result; " + getRow(7));
        System.out.println("result; " + getRow(8));
    }

    public static List<Integer> smartGetRow(int rowIndex) {
        List<Integer> list = new ArrayList<Integer>();

        for (int i = 0; i < rowIndex + 1; i++) {
            list.add(0, 1);
            for (int j = 1; j < list.size() - 1; j++) {
                list.set(j, list.get(j) + list.get(j + 1));
            }
        }
        return list;
    }

    public static List<Integer> getRow(int rowIndex) {
        List<Integer> list = new LinkedList<>();
        if(rowIndex  == 0) {
            list.add(1);
            return list;
        }
        else if(rowIndex == 1) {
            list.add(1);
            list.add(1);
            return list;
        }

        list.add(1);
        list.add(1);
        return getRow(rowIndex, 1, list);

    }

    public static List<Integer> getRow(int index, int level, List<Integer> list) {
        if (index == level) {
            return list;
        }

        List<Integer> newList = new LinkedList<>();
        if (list != null) {
            int count = 0;
            newList.add(count, 1);

            Iterator<Integer> currentIt = list.iterator();
            Iterator<Integer> nextIt = list.iterator();
            if(nextIt.hasNext()) {
                nextIt.next();
                while (nextIt.hasNext()) {
                    count++;
                    newList.add(count, currentIt.next() + nextIt.next());
                }
            }

            newList.add(++count, 1);
        }
        return getRow(index, level + 1, newList);
    }
}
