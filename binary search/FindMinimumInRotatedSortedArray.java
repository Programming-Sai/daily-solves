public class FindMinimumInRotatedSortedArray {
    public int findMin(int[] nums) {
        int l, r, mid, n = nums.length;
        l = 0;
        r = n - 1;
        if (nums[l] <= nums[r]) {
            return nums[l];
        }
        while (l < r) {
            mid = l + (r - l) / 2;
            if (nums[mid] > nums[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return nums[l];
    }

}
