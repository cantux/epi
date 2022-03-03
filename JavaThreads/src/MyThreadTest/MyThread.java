package MyThreadTest;

public class MyThread extends Thread {
    public int count = 0;
    public static int shared = 0;

    @Override
    public void run() {
        System.out.println("Thread starting");

        while(count < 5) {
            try {
                count++;
                shared++;
                System.out.println("Thread id: " + Thread.currentThread().getId()
                        + " Thread name: " + Thread.currentThread().getName()
                        + " count: " + count
                        + " shared: " + shared);
                Thread.sleep(500);
            } catch(InterruptedException e) {
                System.out.println("Thread interrupted: " + Thread.currentThread().getId());
            }
        }

        System.out.println("Thread exiting");
    }
}
