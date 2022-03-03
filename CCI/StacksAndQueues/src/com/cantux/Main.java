package com.cantux;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        Queue<Integer> jQueue = new LinkedList();

        for(int i = 0; i < 10; i++) {
            jQueue.add(i);
        }

        for(int i = 0; i < 10; i++) {
            System.out.println("dequed item is: " + jQueue.remove());
        }

        Stack<Integer> jStack = new Stack();

        for(int i = 0; i < 10; i++) {
            jStack.push(i);
        }
        for(int i = 0; i < 10; i++) {
            System.out.println("Popped item is: " + jStack.pop());
        }
    }
}
