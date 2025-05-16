public class KokoEatingBananas {
    public static int minEatingSpeed(int[] piles, int h) {
        int l, r, time, mid;
        l = 1;
        r = 0;
        time = 0;
        for (int x : piles) {
            if (x > r) {
                r = x;
            }
        }
        // System.out.println(r);
        while (l < r) {
            mid = l + (r - l) / 2;
            time = 0;
            for (int pile : piles) {
                time += (pile + mid - 1) / mid;
            }
            if (time <= h) {
                r = mid; // Why r = mid and nor mid - 1
            } else {
                l = mid + 1; // Why l = mid +1 and not just mid.
            }
        }

        return l;
    }

    public static void main(String[] args) {
        System.out.println(minEatingSpeed(new int[] { 3, 6, 7, 11 }, 8));
        System.out.println(minEatingSpeed(new int[] { 30, 11, 23, 4, 20 }, 5));
        System.out.println(minEatingSpeed(new int[] { 30, 11, 23, 4, 20 }, 6));
    }
}
