
public class TeemoAttacking {

    public static int findPoisonedDuration(int[] timeSeries, int duration) {
        int total = 0;
        for (int i = 1; i < timeSeries.length; i++) {
            total += Math.min(duration, timeSeries[i] - timeSeries[i - 1]);
        }
        return total + duration;
    }

    public static void main(String[] args) {
        System.out.println(findPoisonedDuration(new int[] { 1, 4 }, 2));
        System.out.println(findPoisonedDuration(new int[] { 1, 2 }, 2));
        System.out.println(findPoisonedDuration(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 }, 1));
    }
}