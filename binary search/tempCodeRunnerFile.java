
public class BinaryInsertion {

    public static void main(String[] args) {
        // Fine the first value that is greater than target

        // Fine the first value that is less than target
        int l, r, mid, target;
        boolean isGreaterThan = false;
        int[] arr = new int[] { 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 20 };
        l = 0;
        r = arr.length - 1;
        target = 11;
        mid = l + (r - l) / 2;
        while (l <= r) {
            mid = l + (r - l) / 2;
            if (l == r && l == mid) {
                System.out.println(arr[mid]);
                break;
            } else if (arr[mid] < target) {
                l = mid + (isGreaterThan ? 1 : 0);
            } else if (arr[mid] > target) {
                r = mid + (isGreaterThan ? 0 : -1);
            }
            if (l >= arr.length || r < 0 || l > r)
                break;
            System.out.println(arr[l] + ", " + arr[mid] + ", " + arr[r]);
        }
    }
}
