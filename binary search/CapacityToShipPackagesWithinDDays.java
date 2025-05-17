public class CapacityToShipPackagesWithinDDays {
    public static int shipWithinDays(int[] weights, int days) {
        int l, r, mid, max = Integer.MIN_VALUE, sum = 0, ans = -1;

        for (int weight : weights) {
            if (max < weight) {
                max = weight;
            }
            sum += weight;
        }
        l = max;
        r = sum;

        while (l <= r) {
            mid = l + (r - l) / 2;
            boolean isShippable = ship(mid, days, weights);
            if (isShippable) {
                ans = mid;
                r = mid - 1;

            } else {
                l = mid + 1;

            }
        }
        return ans;
    }

    static boolean ship(int capacity, int days, int[] weights) {
        int daysUsed = 0, rSum = 0;
        for (int weight : weights) {
            if ((rSum + weight > capacity)) {
                rSum = 0;
                daysUsed++;
            }
            rSum += weight;
        }

        if (rSum > 0) {
            daysUsed++;
        }
        return daysUsed <= days;
    }

    public static void main(String[] args) {
        System.out.println(shipWithinDays(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }, 5));
        System.out.println(shipWithinDays(new int[] { 3, 2, 2, 4, 1, 4 }, 3));
        System.out.println(shipWithinDays(new int[] { 1, 2, 3, 1, 1 }, 4));
    }
}
