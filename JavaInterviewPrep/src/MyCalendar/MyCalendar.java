package MyCalendar;

import java.util.*;

class MyCalendar {

    TreeMap<Integer, Integer> calendar;

    public MyCalendar() {
        calendar = new TreeMap<>();
    }

    public boolean book(int start, int end) {

        // find closest start key and get the end of it
        Integer closestStart = calendar.floorKey(start);
        if (closestStart != null && calendar.get(closestStart) > start)
            return false;


        Integer closestEnd = calendar.ceilingKey(start);
        if (closestEnd != null && closestEnd < end) return false;

        calendar.put(start, end);
        return true;
    }
}