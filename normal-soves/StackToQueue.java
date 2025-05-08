import java.util.LinkedList;
import java.util.Queue;

public class StackToQueue {
    Queue<Integer> mainQueue;
    Queue<Integer> tempQueue;

    public StackToQueue() {
        mainQueue = new LinkedList<>();
        tempQueue = new LinkedList<>();
    }

    public void push(int x) {
        while (!mainQueue.isEmpty()) {
            tempQueue.offer(mainQueue.poll());
        }
        mainQueue.offer(x);
        while (!tempQueue.isEmpty()) {
            mainQueue.offer(tempQueue.poll());
        }
    }

    public int pop() {
        return mainQueue.poll();
    }

    public int top() {
        return mainQueue.peek();
    }

    public boolean empty() {
        return mainQueue.isEmpty();
    }
}
