import java.util.Stack;

public class OneThreeTwoPattern {
    public static boolean find132pattern(int[] nums) {
        Stack<Integer> stack = new Stack<>();
        int thirdTracker = Integer.MIN_VALUE;

        for (int i = nums.length - 1; i > -1; i--) {
            if (nums[i] < thirdTracker) {
                // System.out.println(nums[i] + ", " + thirdTracker + ", " + stack.peek());
                return true;
            }

            while (!stack.isEmpty() && nums[i] > stack.peek()) {
                thirdTracker = stack.pop();
            }

            stack.push(nums[i]);
        }
        return false;

    }

    public static void main(String[] args) {
        System.out.println(find132pattern(new int[] { 1, 2, 3, 4 }));
        System.out.println(find132pattern(new int[] { -1, 3, 2, 0 }));
        System.out.println(find132pattern(new int[] { 1, 0, 1, -4, -3 }));
    }
}
