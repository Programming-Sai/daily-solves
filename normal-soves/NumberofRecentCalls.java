import java.util.ArrayDeque;
import java.util.Deque;

public class NumberofRecentCalls {

    Deque<Integer> callDeque;

    public NumberofRecentCalls() {
        callDeque = new ArrayDeque<>();
    }

    public int ping(int t) {
        // System.out.println(callDeque);
        while (!callDeque.isEmpty() && (t - 3000) > callDeque.peekFirst()) {
            callDeque.pop();
        }
        callDeque.add(t);
        return callDeque.size();
    }

    public static void main(String[] args) {
        NumberofRecentCalls recentCounter = new NumberofRecentCalls();
        System.out.println(recentCounter.ping(1)); // Output: 1
        System.out.println(recentCounter.ping(100)); // Output: 2
        System.out.println(recentCounter.ping(3001)); // Output: 3
        System.out.println(recentCounter.ping(3002)); // Output: 3
    }
}