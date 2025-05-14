import java.util.Arrays;

public class FindFirstAndLastPositionOfElementInSortedArray {
    public static int[] searchRange(int[] nums, int target) {
        int l1, r1, mid1, ans1;
        l1 = 0;
        r1 = nums.length - 1;
        ans1 = -1;
        while (l1 <= r1) {
            mid1 = l1 + (r1 - l1) / 2;
            if (nums[mid1] >= target) {
                ans1 = mid1;
                r1 = mid1 - 1;
            } else {
                l1 = mid1 + 1;
            }
        }

        int l2, r2, mid2, ans2;
        l2 = 0;
        r2 = nums.length - 1;
        ans2 = -1;

        while (l2 <= r2) {
            mid2 = l2 + (r2 - l2) / 2;
            if (nums[mid2] <= target) {
                ans2 = mid2;
                l2 = mid2 + 1;
            } else {
                r2 = mid2 - 1;
            }
        }
        if (ans1 == -1 || ans2 == -1 || nums[ans1] != target || nums[ans2] != target) {
            return new int[] { -1, -1 };
        }

        return new int[] { ans1, ans2 };

    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 7, 8, 8, 10 }, 7)));
        System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 7, 8, 8, 10 }, 10)));
        System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 7, 8, 8, 10 }, 5)));
        System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 7 }, 7)));
        System.out.println(Arrays.toString(searchRange(new int[] { 7, 7, 7, 9 }, 7)));
        System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 8, 8, 10 }, 11)));
        System.out.println();
        // Test cases

        // 1. Target not in the array
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 2, 3, 4, 5 }, 6))); // [-1, -1]

        // 2. Single element array (target present)
        System.out.println(Arrays.toString(searchRange(new int[] { 5 }, 5))); // [0, 0]

        // 3. Single element array (target absent)
        System.out.println(Arrays.toString(searchRange(new int[] { 10 }, 5))); // [-1, -1]

        // 4. All elements are the target
        System.out.println(Arrays.toString(searchRange(new int[] { 7, 7, 7, 7 }, 7))); // [0, 3]

        // 5. Empty array
        System.out.println(Arrays.toString(searchRange(new int[] {}, 5))); // [-1, -1]

        // 6. Target is larger than all elements
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 2, 3, 4, 5 }, 6))); // [-1, -1]

        // 7. Target is smaller than all elements
        System.out.println(Arrays.toString(searchRange(new int[] { 6, 7, 8, 9, 10 }, 5))); // [-1, -1]

        // 8. Target is between duplicates
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 2, 3, 3, 3, 4 }, 3))); // [2, 4]

        // 9. Target is at the end of the array
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 2, 3, 4, 5 }, 5))); // [4, 4]

        // 10. Target at the beginning of the array
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 2, 3, 4, 5 }, 1))); // [0, 0]

        // 11. Multiple occurrences of the target with gaps
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 3, 5, 7, 7, 9, 10 }, 7))); // [3, 4]

        // 12. Target is exactly between two values
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 3, 5, 7, 9 }, 6))); // [-1, -1]

        // 13. Target is one occurrence among many larger elements
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 3, 3, 4, 5 }, 1))); // [0, 0]
        System.out.println(Arrays.toString(searchRange(new int[] { 1, 3, 3, 4, 5 }, 5))); // [4, 4]

        // 14. Descending array
        System.out.println(Arrays.toString(searchRange(new int[] { 10, 9, 8, 7, 6 }, 7))); // [-1, -1]

    }
}
