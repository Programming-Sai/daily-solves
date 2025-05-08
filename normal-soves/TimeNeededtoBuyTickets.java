import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;

public class TimeNeededtoBuyTickets {

    public static int timeRequiredToBuy(int[] tickets, int k) {
        Deque<Integer> ticketsDeque = new ArrayDeque<>();
        HashMap<Integer, Integer> kVal = new HashMap<>();
        kVal.put(tickets[k], k);

        for (int ticket : tickets) {
            ticketsDeque.offer(ticket);
        }
        // System.out.println(ticketsDeque);
        while (tickets[k] != 0) {
            int front = ticketsDeque.poll() - 1;
            ticketsDeque.offer(front);
            // System.out.println(ticketsDeque);
            k--;
            k = ((k % ticketsDeque.size()) + ticketsDeque.size()) % ticketsDeque.size();
            System.out.println(k);
        }
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(timeRequiredToBuy(new int[] { 2, 3, 2 }, 0));
    }
}
