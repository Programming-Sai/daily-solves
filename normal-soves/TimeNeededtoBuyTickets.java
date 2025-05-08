import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;

public class TimeNeededtoBuyTickets {

    public static int timeRequiredToBuy(int[] tickets, int k) {
        int n = tickets.length;
        int i = -1;
        int c = 0;
        System.out.println(Arrays.toString(tickets));
        while (true) {
            i++;
            i = (i % n);

            if (tickets[i] == 0) {
                continue;
            }
            tickets[i]--;
            System.out.println(Arrays.toString(tickets));
            c++;

            if (i == k) {
                if (tickets[i] == 0) {
                    break;
                }
            }

        }

        return c;
    }

    public static void main(String[] args) {
        System.out.println(timeRequiredToBuy(new int[] { 2, 3, 2 }, 2));
        // System.out.println(timeRequiredToBuy(new int[] { 5, 1, 1, 1 }, 0));
    }
}
