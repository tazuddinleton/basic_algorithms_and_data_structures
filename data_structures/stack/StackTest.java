public class StackTest {
    public static void main(String[] args) {
        Stack stack = new Stack();

        System.out.println("Size: " + stack.size());
        System.out.println("is full: " + stack.isFull());
        System.out.println("is empty: " + stack.isEmpty());
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        stack.push(6);

        System.out.println(stack.toString());
        System.out.println("Top: " + stack.peek());
        System.out.println("Popped: " + stack.pop());
        System.out.println("Popped: " + stack.pop());
        System.out.println(stack.toString());

        System.out.println("Size: " + stack.size());
        System.out.println("is full: " + stack.isFull());
        System.out.println("is empty: " + stack.isEmpty());
        System.out.println("index of 2 : " + stack.indexOf(2));
        System.out.println("index of 4 : " + stack.indexOf(4));
    }
}