
/**
 * 1. push() 2. pop() 3. peek() 4. find() 5. size() 6. isFull() 7. isEmpty()
 */
public class Stack {
    private final int MAX = 10;
    private int count;
    private Node top;

    public Stack() {
        this.count = 0;
        this.top = new Node();
    }

    public void push(Object data) {
        Node n = new Node(data, top);
        top = n;
        count++;
    }

    public Object pop() {
        Object data = this.top.data();
        top = this.top.next();
        count--;
        return data;
    }

    public Object peek() {
        return this.top.data();
    }

    public int size() {
        return this.count;
    }

    public boolean isFull() {
        return this.count == this.MAX;
    }

    public boolean isEmpty() {
        return this.count == 0;
    }

    public int indexOf(Object data) {
        int terminator = 0;
        Node temp = top;
        while (temp.next() != null) {
            if (temp.data().equals(data)) {
                return terminator;
            }
            temp = temp.next();
            terminator++;
        }
        return -1;
    }

    public String toString() {
        Node temp = top;
        StringBuffer str = new StringBuffer();
        while (temp.next() != null) {
            str.append(temp.data().toString() + ", ");
            temp = temp.next();
        }
        return str.toString();
    }
}

class Node {
    private Node next;
    private Object data;

    public Node() {
    }

    public Node(Object data, Node next) {
        this.data = data;
        this.next = next;
    }

    public Node next() {
        return this.next;
    }

    public void next(Node next) {
        this.next = next;
    }

    public Object data() {
        return this.data;
    }
}