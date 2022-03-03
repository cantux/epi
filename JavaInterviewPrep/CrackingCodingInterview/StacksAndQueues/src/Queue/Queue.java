package Queue;

public class Queue<T> {
    public class QueueNode<T> {
        public QueueNode<T> next;
        public T data;

        public QueueNode(T data) {
            this.data = data;
        }
    }

    QueueNode<T> first;
    QueueNode<T> last;

    public void enqueue(T data) {
        QueueNode<T> node = new QueueNode(data);
        if(last != null)
        {
            last.next = node;
        }
        last = node;
        if(first == null) {

            first = last;
        }
    }

    public T deq() {
        T data = first.data;

        first = first.next;
        if(first == null) {
            last = null;
        }
        return data;
    }
}
