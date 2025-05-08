import java.util.Arrays;

public class DesignCircularDeque {
    private int[] deque;
    private int front;
    private int end;
    private int capacity;
    private int size;

    public DesignCircularDeque(int k) {
        deque = new int[k];
        capacity = k;
        front = 0;
        end = 0;
        size = 0;
    }

    public boolean insertFront(int value) {
        System.out.println(Arrays.toString(deque));
        if (isFull()) {
            return false;
        }
        front = (front - 1 + capacity) % capacity;
        deque[front] = value;
        size++;
        System.out.println(Arrays.toString(deque) + ", " + size + ", " + front + ", " + end);
        return true;
    }

    public boolean insertLast(int value) {
        System.out.println(Arrays.toString(deque));
        if (isFull()) {
            return false;
        }
        deque[end] = value;
        end = (end + 1) % capacity;
        size++;
        System.out.println(Arrays.toString(deque) + ", " + size + ", " + front + ", " + end);
        return true;
    }

    public boolean deleteFront() {
        size--;
        if (isEmpty()) {
            return false;
        }
        front = (front + 1 + capacity) % capacity;
        return true;
    }

    public boolean deleteLast() {
        size--;
        if (isEmpty()) {
            return false;
        }
        end = (end - 1 + capacity) % capacity;
        return true;
    }

    public int getFront() {
        return deque[front];
    }

    public int getRear() {
        return deque[end];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }

    void printDeque() {
        int i = front;
        int count = 0;
        while (count < size) {
            System.out.print(deque[i] + " ");
            i = (i + 1) % capacity;
            count++;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Test case 1: Create a deque with capacity 3
        DesignCircularDeque deque = new DesignCircularDeque(3);

        // Test case 2: Insert elements at the front and the rear
        System.out.println("Insert at front 1: " + deque.insertFront(1)); // Should be true
        System.out.println("Insert at last 2: " + deque.insertLast(2)); // Should be true
        System.out.println("Insert at front 3: " + deque.insertFront(3)); // Should be true
        System.out.println("Insert at front 4: " + deque.insertFront(4)); // Should be false (deque is full)

        // Test case 3: Check the front and rear elements
        System.out.println("Front: " + deque.getFront()); // Should be 3
        System.out.println("Rear: " + deque.getRear()); // Should be 2

        deque.printDeque();

        // Test case 4: Delete elements from the front and rear
        System.out.println("Delete front: " + deque.deleteFront()); // Should be true
        System.out.println("Delete last: " + deque.deleteLast()); // Should be true

        // Test case 5: Check the front and rear elements after deletion
        System.out.println("Front: " + deque.getFront()); // Should be 1
        System.out.println("Rear: " + deque.getRear()); // Should be 1

        // // Test case 6: Try inserting again after deletions
        // System.out.println("Insert at front 5: " + deque.insertFront(5)); // Should
        // be true
        // System.out.println("Insert at last 6: " + deque.insertLast(6)); // Should be
        // true

        // // Test case 7: Check if the deque is full
        // System.out.println("Is full? " + deque.isFull()); // Should be true

        // // Test case 8: Delete the remaining elements and check if empty
        // System.out.println("Delete front: " + deque.deleteFront()); // Should be true
        // System.out.println("Delete front: " + deque.deleteFront()); // Should be true
        // System.out.println("Is empty? " + deque.isEmpty()); // Should be true
    }
}
