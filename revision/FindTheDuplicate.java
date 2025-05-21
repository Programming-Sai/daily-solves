
import java.util.Arrays;
import java.util.HashMap;

public class FindTheDuplicate {
    public static int findDuplicate(int[] nums) {
        HashMap<Integer, Integer> frequencies = new HashMap<>();
        int target = -1, l, r, mid, n = nums.length;
        for (int num : nums) {
            frequencies.put(num, frequencies.getOrDefault(num, 0) + 1);
        }
        for (int num : nums) {
            // System.out.println(num + ", " + frequencies.get(num));
            if (frequencies.get(num) > 1) {
                target = num;
            }
        }
        // System.out.println(Arrays.toString(nums));

        l = 1;
        r = n - 1;
        // System.out.println(l + ", " + r + ", " + target);
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
        System.out.println(findDuplicate(new int[] { 3, 1, 3, 4, 2 }));
        System.out.println(findDuplicate(new int[] { 3, 3, 3, 3, 3 }));
    }

}