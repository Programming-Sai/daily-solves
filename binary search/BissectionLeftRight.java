
public class BissectionLeftRight {

    // public static void main(String[] args) {

    // int l, r, mid, target;

    // // Fine the first value that is greater than target
    // boolean isGreaterThan = true;

    // // Fine the first value that is less than target
    // // boolean isGreaterThan = false;
    // int[] arr = new int[] { 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 20, 25, 30 };
    // l = 0;
    // r = arr.length - 1;
    // target = 11;
    // while (l <= r) {
    // mid = l + ((r - l) / 2);
    // if (l == r && l == mid && r == mid) {
    // System.out.println(arr[mid]);
    // break;
    // } else if (arr[mid] < target) {
    // l = mid + (isGreaterThan ? 1 : 0);
    // } else if (arr[mid] > target) {
    // r = mid + (isGreaterThan ? 0 : -1);
    // }
    // if (l >= arr.length || r < 0 || l > r) {
    // break;
    // }
    // // System.out.println(arr[l] + ", " + arr[mid] + ", " + arr[r] + ", " + mid);
    // }
    // }

    public static int bissection(int[] arr, int target, String type) {
        int l, r, mid;
        // boolean isGreaterThan = true; // True -> Bisset right
        // boolean isGreaterThan = false; // False -> Bisset left
        boolean isGreaterThan = type.equals("right");

        l = 0;
        r = arr.length - 1;

        int result = -1;
        while (l <= r) {
            mid = l + ((r - l) / 2);
            if (isGreaterThan) {
                if (arr[mid] > target) {
                    result = mid;
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                if (arr[mid] < target) {
                    result = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }

        if (result != -1) {
            // System.out.println(arr[result]);
            return arr[result];
        } else {
            // System.out.println("No valid value found.");
            return -1;
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[] { 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 20 };
        int target = 11;

        System.out.println(bissection(arr, target, "right"));
        System.out.println(bissection(arr, target, "left"));

    }
}
