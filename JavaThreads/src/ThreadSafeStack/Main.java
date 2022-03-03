package ThreadSafeStack;

import java.util.*;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;

public class Main {
    public static void main(String[] args) {
        Stack s = new Stack<Integer>(30);
        Thread[] pt = new Thread[3];
        Thread[] ct = new Thread[3];
        for(int i = 0; i < 3; i++) {
            pt[i] = new Thread(new Producer(s), "producer " + i);
            pt[i].start();
            ct[i] = new Thread(new Consumer(s), "consumer " + i);
            ct[i].start();
        }

        try {
            for(int i = 0; i < 3; i++) {
                ct[i].join();
                pt[i].join();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

class Stack<T> {
    List<T> list;

    Semaphore semAdd;
    Semaphore semRemove;

    ReentrantLock mutex;

    public Stack(int capacity) {
        list = new ArrayList<T>();
        semAdd = new Semaphore(capacity);
        semRemove = new Semaphore(0);
        mutex = new ReentrantLock();
    }

    public void push(T x) {

        try {
            semAdd.acquire();
            mutex.lock();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        list.add(x);
        System.out.println(Arrays.toString(list.toArray()));
        mutex.unlock();
        semRemove.release();
    }

    public T pop() {
        try {
            semRemove.acquire();
            mutex.lock();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        T obj = list.remove(list.size() - 1);
        System.out.println("remove permits: " + semRemove.availablePermits());
        System.out.println("removed: " + " from thread: " + Thread.currentThread().getId());
        System.out.println(Arrays.toString(list.toArray()));
        mutex.unlock();
        semAdd.release();
        return obj;
    }

    public T peek() {
        T obj = list.get(list.size() - 1);
        return obj;
    }

    public void pushMulti(List<T> list) {
        try {
            semAdd.acquire(list.size());
            mutex.lock();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        list.addAll(list);
        System.out.println(Arrays.toString(list.toArray()));
        mutex.unlock();
        semRemove.release(list.size());
    }

    public List<T> popMulti(int size) {
        try {
            semRemove.acquire();
            mutex.lock();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        List<T> list = new ArrayList<T>();
        for(int i = 0; i < size; i++) {
            list.add(list.remove(list.size() - 1));
        }

        System.out.println("remove permits: " + semRemove.availablePermits());
        System.out.println("removed: " + " from thread: " + Thread.currentThread().getId());
        System.out.println(Arrays.toString(list.toArray()));
        mutex.unlock();
        semAdd.release();
        return list;
    }
}

class Producer implements Runnable {
    Stack s;
    static int inc = 0;
    public Producer(Stack s) {
        this.s = s;
    }
    public void run() {
        for(int i = 0; i < 30; i++) {
            s.push(inc++);
            try {
                Thread.sleep(i * 100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class Consumer implements Runnable {
    Stack s;
    public Consumer(Stack s) {
        this.s = s;
    }
    public void run() {
        for(int i = 29; i >= 0; i--) {
            s.pop();
            try {
                Thread.sleep(i * 100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
