package StackMin;

import java.util.Stack;

public class StackMinEf extends Stack<Integer>{
    public Stack<Integer> minStack = new Stack();

    public int push(int item)
    {
        // SEE THE FREAKIN TRICK WITH EQUALS!!!!
        if(item <= min()) {
            minStack.push(item);
        }
        return super.push(item);
    }

    public Integer pop()
    {
        int poppedItem = super.pop();
        if(poppedItem == min()) {
            minStack.pop();
        }
        return poppedItem;
    }

    public int min() {
        if(super.isEmpty()) {
            return Integer.MAX_VALUE;
        }
        else{
            return minStack.peek();
        }
    }
}


