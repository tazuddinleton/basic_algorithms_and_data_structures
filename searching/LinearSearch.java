package searching;

public class LinearSearch {
    private Object[] data;
    private int count;

    public LinearSearch(int size) {
        this.data = new Object[size];
        this.count = 0;
    }

    public void add(Object data) {
        this.data[count] = data;
        this.count++;
    }

    public void remove(Object data) {
        int terminator = 0;
        while (terminator < this.count) {
            if (this.data[terminator] == data) {
                while (terminator < this.count) {
                    this.data[terminator] = this.data[terminator + 1];
                    terminator++;
                }
                this.count--;
            }
            terminator++;
        }
    }

    public void display() {
        int terminator = 0;
        while (terminator < this.count) {
            System.out.println(this.data[terminator]);
            terminator++;
        }
    }

    public int indexOf(Object data) {
        int terminator = 0;
        while (terminator < this.count) {
            if (this.data[terminator] == data) {
                return terminator;
            }
            terminator++;
        }
        return -1;
    }

}