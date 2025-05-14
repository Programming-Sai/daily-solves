import java.util.Arrays;

public class FindFirstAndLastPositionOfElementInSortedArray {
    public static int[] searchRange(int[] nums, int target) {
        int l1, r1, mid1, ans1;
        l1 = 0;
        r1 = nums.length - 1;
        ans1 = -100;
        while (l1 <= r1) {
            mid1 = l1 + (r1 - l1) / 2;
            if (nums[mid1] < target) {
                ans1 = mid1;
                l1 = mid1 + 1;
            } else {
                r1 = mid1 - 1;
            }
        }

        int l2, r2, mid2, ans2;
        l2 = 0;
        r2 = nums.length - 1;
        ans2 = -100;

        while (l2 <= r2) {
            mid2 = l2 + (r2 - l2) / 2;
            if (nums[mid2] > target) {
                ans2 = mid2;
                r2 = mid2 - 1;
            } else {
                l2 = mid2 + 1;
            }
        }

        return new int[] { ans1 == -100 ? -1 : ans1 + 1, ans2 == -100 ? -1 : ans2 - 1 };

    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 7, 8, 8, 10 }, 7)));
        System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 7, 8, 8, 10 }, 10)));
        // System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 7 },
        // 7)));
        // System.out.println(Arrays.toString(searchRange(new int[] { 5, 7, 7, 8, 8, 10
        // }, 6)));
    }
}
