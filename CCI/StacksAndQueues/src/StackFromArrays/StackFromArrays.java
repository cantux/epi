package StackFromArrays;

import java.util.Stack;

public class StackFromArrays<T> extends Stack<T> {

    public T[] array;

    public StackFromArrays() {
        super();
    }

    @Override
    public T push(T item) {
        return super.push(item);
    }

    @Override
    public synchronized T pop() {
        return super.pop();
    }

    @Override
    public synchronized T peek() {
        return super.peek();
    }

    @Override
    public boolean empty() {
        return super.empty();
    }

    @Override
    public synchronized int search(Object o) {
        return super.search(o);
    }
}


