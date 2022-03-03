package StackMin;

public class StackMinTest {

    public static void main(String[] args) {
        StackMin stm0 = new StackMin();
        StackMin stm1 = new StackMin();
        for(int i = 0; i < 10; i++) {
            stm0.push(i);
        }

        for(int i = 0; i < 10; i++) {
            System.out.println("stm0 min before pop: " + stm0.min());
            stm1.push(stm0.pop());
        }

        for(int i = 0; i < 10; i++) {
            System.out.println("stm1 min before pop: " + stm1.min());
            stm1.pop();
        }

        StackMinEf ef0 = new StackMinEf();
        StackMinEf ef1 = new StackMinEf();
        for(int i = 0; i < 10; i++) {
            ef0.push(i);
        }

        for(int i = 0; i < 10; i++) {
            System.out.println("ef0 min before pop: " + ef0.min());
            ef1.push((int)ef0.pop());
            System.out.println("ef1 min after push: " + ef1.min());
        }

        for(int i = 0; i < 10; i++) {
            System.out.println("ef1 min before pop: " + ef1.min());
            ef1.pop();
        }
    }
}
