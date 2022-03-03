package MyThreadTest;


public class Main {

    public static void main(String[] args) {
        MyThread t1 = new MyThread();
        t1.start();

        MyThread t2 = new MyThread();
        t2.start();

        while(t1.count < 5) {
            try {
                Thread.sleep(250);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("shared: " + t2.shared);
        System.out.println("main exiting");
    }
}
