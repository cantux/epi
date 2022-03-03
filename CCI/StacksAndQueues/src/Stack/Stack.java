package Stack;

public class Stack<T> {
    public class StackNode<T> {
        public StackNode<T> next;
        public T data = null;

        public StackNode(T data) {
            this.data = data;
        }
    }

    StackNode<T> top;

    public void push(T data) {
        StackNode<T> node = new StackNode(data);
        node.next = top;
        top = node;
    }

    public T pop() {
        if(top != null) {
            T data = top.data;
            top = top.next;
            return data;
        }
        return null;
    }

    public T peek() {
        if(top != null) {
            return top.data;
        }
        return null;
    }

    public static void main(String[] args) {
        Stack<Integer> s = new Stack();

        System.out.println("pop empty: " + s.pop());
        System.out.println("peek empty: " + s.peek());

        s.push(1);
        s.push(2);
        System.out.println("peek 2: " + s.peek());
        System.out.println("pop 2: " + s.pop());
        System.out.println("peek 1: " + s.peek());
        System.out.println("pop 1: " + s.pop());

    }
}
