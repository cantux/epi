package TowersOfHanoi;

import java.util.Stack;

public class Tower {
    private Stack<Integer> disks;

    private int index;

    public Tower(int i) {
        disks = new Stack<>();
        index = i;
    }

    public int index() {
        return index;
    }

    public void add(int d) {
        if(!disks.isEmpty() && disks.peek() <= d) {
            System.out.println("error placing disk: " + d);
        }
        else {
            disks.push(d);
        }
    }

    public void moveTopTo(Tower t) {
        int top = disks.pop();
        t.add(top);
    }

    public void moveDisks(int n, Tower dest, Tower buff) {
        if(n > 0) {
            moveDisks(n -1, buff, dest);
            moveTopTo(dest);
            buff.moveDisks(n - 1, dest, this);
        }
    }

    public void printDisks() {
        disks.forEach(e -> System.out.println("elem: " + e));
    }
}