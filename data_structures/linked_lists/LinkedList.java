package data_structures.linked_lists;

public class LinkedList {
    private int count;
    private Node root;

    public LinkedList() {
        this.count = 0;
        this.root = new Node();
    }

    public int add(Object data) {
        Node n = new Node(data, root);
        this.root = n;
        increment();
        return size();
    }

    public int size() {
        return this.count;
    }

    public boolean remove(Object data) {
        Node curr = null;
        Node prev = null;
        curr = root;
        while (curr.next() != null) {
            if (curr.data() == data) {
                if (prev != null) {
                    prev.next(curr.next());
                }
                root = curr.next();
                decrement();
                return true;
            }
            curr = curr.next();
        }
        return false;
    }

    public void display() {
        Node temp = this.root;
        while (temp.next() != null) {
            System.out.println(temp.data());
            temp = temp.next();
        }

    }

    private void increment() {
        this.count++;
    }

    private void decrement() {
        this.count--;
    }

}

class Node {

    private Object data;
    private Node next;

    public Node() {
    }

    public Node(Object data, Node next) {
        this.data = data;
        this.next = next;
    }

    public Node next() {
        return this.next;
    }

    public Object data() {
        return this.data;
    }

    public void next(Node next) {
        this.next = next;
    }
}