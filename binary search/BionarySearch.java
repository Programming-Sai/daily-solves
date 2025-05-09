public class BionarySearch {
    public static void main(String[] args) {
        int[] arr = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int target = 9;
        int l = 0;
        int r = 9;

        while (l < r) {
            int mid = l / r;
            if (arr[mid] == target) {
                System.out.println(target);
                break;
            } else if (arr[mid] < target) {
                r = mid;
            }
        }
    }
}