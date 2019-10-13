package searching;

public class LinearSearchTest {
    public static void main(String[] args) {
        LinearSearch li = new LinearSearch(10);

        li.add(1);
        li.add(2);
        li.add(3);
        li.add(4);

        li.remove(2);
        li.remove(4);
        li.display();

        int i1 = li.indexOf(3);
        int i2 = li.indexOf(10);

        System.out.printf("index of 3 is %d and index of 10 is %d", i1, i2);
    }
}