public class FindPeakElement {
    public static int findPeakElement(int[] nums) {
        int l, r, mid, n = nums.length;

        if (n == 1 || nums[0] > nums[1]) {
            return 0;
        } else if (nums[n - 2] < nums[n - 1]) {
            return n - 1;
        }

        l = 0;
        r = n - 1;
        while (l < r) {
            mid = l + (r - l) / 2;
            System.out.println(mid);
            if (mid > 0 && mid < n && nums[mid - 1] < nums[mid] && nums[mid] > nums[mid + 1]) {
                return mid;
            }
            if (nums[mid] < nums[mid + 1]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        // Since l == r at this point we can return any of them.
        return l;
    }

    public static void main(String[] args) {
        // System.out.println(findPeakElement(new int[] { 1, 2, 3, 1 }));
        System.out.println(findPeakElement(new int[] { 1, 2, 1, 3, 5, 6, 4 }));
    }
}
