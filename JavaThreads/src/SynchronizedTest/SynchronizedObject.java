package SynchronizedTest;

public class SynchronizedObject {
    public synchronized void say(String message) {
        try {
            int count = 5;
            System.out.println("hello start on: " + Thread.currentThread().getId());
            while(count > 0) {
                System.out.println("message: " + message + " from: " + Thread.currentThread().getId());
                Thread.sleep(3000);
                count--;
            }
            System.out.println("hello end on: " + Thread.currentThread().getId());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


}
