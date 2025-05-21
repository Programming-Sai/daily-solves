
import java.util.Arrays;
import java.util.HashMap;

public class FindTheDuplicate {
    public static int findDuplicate(int[] nums) {
        HashMap<Integer, Integer> frequencies = new HashMap<>();
        int target = -1, l, r, mid, n = nums.length;
        for (int i : nums) {
            frequencies.put(nums[i], frequencies.getOrDefault(nums[i], 0) + 1);
        }
        System.out.println(Arrays.toString(nums));
        for (int i : nums) {
            System.out.println(nums[i] + ", " + frequencies.get(nums[i]));
            if (frequencies.get(nums[i]) > 1) {
                target = nums[i];
            }
        }

        l = 1;
        r = n - 1;
        System.out.println(l + ", " + r + ", " + target);
        while (l < r) {
            mid = l + (r - l) / 2;
            if (mid == target) {
                return mid;
            } else if (mid > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }

    public static void main(String[] args) {
        System.out.println(findDuplicate(new int[] { 1, 3, 4, 2, 2 }));
        // System.out.println(findDuplicate(new int[] { 3, 1, 3, 4, 2 }));
        // System.out.println(findDuplicate(new int[] { 3, 3, 3, 3, 3 }));
    }

}