public class BionarySearch {
    public static void main(String[] args) {
        int[] arr = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int target = 1;
        int l = 0;
        int r = arr.length - 1;
        int numberOfOperations = 0;
        boolean found = false;
        int mid;
        while (l <= r) {
            mid = l + (r - l) / 2;
            System.out.println(l + ", " + mid + ", " + r);
            if (arr[mid] == target) {
                System.out.println(target);
                found = true;
                break;
            } else if (arr[mid] < target) {
                l = mid + 1;
            } else if (arr[mid] > target) {
                r = mid - 1;
            }
            numberOfOperations++;
        }
        if (found) {
            System.out.println("Target " + target + " found in " + numberOfOperations + " operations.");
        } else {
            System.out.println("Target " + target + " not found.");
        }
    }
}