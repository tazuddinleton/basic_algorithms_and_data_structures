public class DoublyLinkedList {
    private int count;
    private Link head;
    private Link tail;

    public DoublyLinkedList() {
        this.count = 0;
        this.head = new Link();
        this.tail = new Link();
    }

    public void addToHead(Object data) {
        Link next = new Link(data, this.head, null);
        this.head = next;
        if (isEmpty()) {
            this.tail = next;
        }
        this.count++;
    }

    public void addToTail(Object data) {

        Link next = new Link(data, null, this.tail);
        this.tail = next;
        this.count++;
    }

    private boolean isEmpty() {
        return this.count == 0;
    }

    public void display() {
        int terminator = 0;
        Link temp = this.head;
        while (terminator < this.count) {
            System.out.println("index: " + terminator + " data: " + temp.data() + " head " + this.head.data() + " tail "
                    + this.tail.data());
            temp = temp.next();
            terminator++;
        }
    }
}

class Link {
    private Link next;
    private Link prev;
    private Object data;

    public Link() {
    }

    public Link(Object data, Link next, Link prev) {
        this.next = next;
        this.prev = prev;
        this.data = data;
    }

    public Link prev() {
        return this.prev;
    }

    public Link next() {
        return this.next;
    }

    public Object data() {
        return this.data;
    }

    public void next(Link next) {
        Link t = this.next;
        this.next = next;
        if (next != null) {
            next.prev(t);
        }
    }

    public void prev(Link prev) {
        Link t = this.prev;
        this.prev = prev;
        if (prev != null) {
            prev.next(t);
        }
    }

}