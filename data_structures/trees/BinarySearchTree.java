package data_structures.trees;

/**
 * 1. insert 2. find 3. traversal a. ordered traversal b. inordered traversal.
 * 
 * Ordered traversal : root -> left -> right. InOrdred traversal : left -> root.
 * -> right.
 */

public class BinarySearchTree {
    public static void main(String[] args) {
        int[] arr = new int[] { 1, 2, 1, 5, 5, 3, 3, 3, 4 };

        Node tree = new Node(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            tree.insert(arr[i]);
        }

        tree.printInOrder();

    }
}

class Node {
    int data;
    Node left, right;

    public Node(int value) {
        this.data = value;
    }

    public void insert(int value) {

        if (value <= data) {
            if (left != null) {
                left.insert(value);
            } else {
                left = new Node(value);
            }
        } else {
            if (right != null) {
                right.insert(value);
            } else {
                right = new Node(value);
            }
        }
    }

    public void printInOrder() {
        if (left != null) {
            left.printInOrder();
        }
        System.out.println(data);
        if (right != null) {
            right.printInOrder();
        }
    }
}