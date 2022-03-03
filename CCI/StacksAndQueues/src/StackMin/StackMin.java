package StackMin;

import java.util.Enumeration;
import java.util.Stack;

public class StackMin extends Stack<Integer> {
    public int min;

    public int push(int item)
    {
        if(item < min) {
            min = item;
        }
        return super.push(item);
    }

    public Integer pop()
    {
        // make a search for the smallest
        int poppedItem = super.pop();

        if(poppedItem == min) {
            Enumeration<Integer> en = super.elements();
            int smallest = Integer.MAX_VALUE;
            while(en.hasMoreElements())
            {
                int elem = en.nextElement();
                if(elem < smallest) {
                    smallest = elem;
                }
            }
            min = smallest;
        }
        return poppedItem;
    }

    public int min() {
        if(super.isEmpty()) {
            return Integer.MAX_VALUE;
        }
        else{
            return min;
        }
    }
}
