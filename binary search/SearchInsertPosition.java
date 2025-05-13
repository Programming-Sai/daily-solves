public class SearchInsertPosition {
    public static int searchInsert(int[] nums, int target) {
        int left, right, mid, n;
        left = 0;
        n = nums.length;
        right = n - 1;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    public static void main(String[] args) {
        System.out.println(searchInsert(new int[] {}, 0));
    }
}
