package SynchronizedTest;

public class SynchronizedUser implements Runnable {
    SynchronizedObject sameInstance = null;
    static SynchronizedObject staticInstance = new SynchronizedObject();
    public SynchronizedUser() {
        sameInstance = new SynchronizedObject();
    }
    @Override
    public void run() {
        System.out.println("Runnable running" + Thread.currentThread().getId());

        SynchronizedObject newInstance = new SynchronizedObject();
        newInstance.say("different instance");
//
//        sameInstance.say("same instance");
//
//        staticInstance.say("static instance");
        System.out.println("Runnable exiting"+ Thread.currentThread().getId());

    }
}
