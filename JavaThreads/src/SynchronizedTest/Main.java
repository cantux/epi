package SynchronizedTest;

public class Main {
    public static void main(String[] args) {
        SynchronizedUser r1 = new SynchronizedUser();
        SynchronizedUser r2 = new SynchronizedUser();

        Thread t1 = new Thread(r1, "r1");
        t1.start();

        Thread t11 = new Thread(r1, "r1");
        t11.start();

        Thread t2 = new Thread(r2, "r2");
        t2.start();

        try {
            t1.join();
            t11.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }
}
