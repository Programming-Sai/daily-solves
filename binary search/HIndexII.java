public class HIndexII {
    public static int hIndex(int[] citations) {
        int l, r, mid, n, ans;
        n = citations.length;
        l = 0;
        r = n - 1;
        ans = 0;
        while (l <= r) {
            mid = l + (r - l) / 2;
            if (citations[mid] > mid + 1) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        // if (ans != -1) {
        return citations[ans < 0 ? 0 : ans];
        // }
    }

    public static void main(String[] args) {
        // System.out.println(hIndex(new int[] { 0, 1, 3, 5, 6 }));
        // System.out.println(hIndex(new int[] { 0 }));
        System.out.println(hIndex(new int[] { 1 }));
        // System.out.println(hIndex(new int[] { 1, 2, 100 }));
        // System.out.println(hIndex(new int[] { 3, 4, 5, 8, 10 }));
        // System.out.println(hIndex(new int[] { 3, 3, 5, 8, 25 }));
    }
}
