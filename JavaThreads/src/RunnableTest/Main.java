package RunnableTest;

public class Main {

    public static void main(String[] args) {
        MyRunnable r1 = new MyRunnable();
        MyRunnable r2 = new MyRunnable();

        Thread t1 = new Thread(r1, "r1");
        t1.start();

        Thread t11 = new Thread(r1, "r1");
        t11.start();

        Thread t2 = new Thread(r2, "r2");
        t2.start();

        while(r1.count < 5) {
            try {
                Thread.sleep(250);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
//            System.out.println("shared: " + r1.shared);
        }


        try {
            t1.join();
            t11.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("shared: " + r1.shared);
        System.out.println("main exiting");
    }
}
