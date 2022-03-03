package RunnableTest;

public class MyRunnable implements Runnable {
    public static int shared = 0;
    public int count = 0;

    @Override
    public void run() {
        System.out.println("Runnable running" + Thread.currentThread().getId());

        try {
            while(count < 5) {
                count++;
                shared++;
                System.out.println("Thread id: " + Thread.currentThread().getId()
                        + " Thread name: " + Thread.currentThread().getName()
                        + " count: " + count
                        + " shared: " + shared);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
            System.out.println("runnable interrupted");
        }

        System.out.println("Runnable exiting");

    }
}
