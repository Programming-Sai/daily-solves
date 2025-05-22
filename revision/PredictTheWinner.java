public class PredictTheWinner {

    public static boolean predictTheWinner(int[] nums) {
        return maxDiff(0, nums.length - 1, nums) >= 0;
    }

    static int maxDiff(int left, int right, int[] nums) {
        if (left == right) {
            return nums[left];
        }
        int leftChoice = nums[left] - maxDiff(left + 1, right, nums);
        int rightChoice = nums[right] - maxDiff(left, right - 1, nums);
        return Math.max(leftChoice, rightChoice);
    }

    public static void main(String[] args) {
        System.out.println(predictTheWinner(new int[] { 1, 5, 2 }));
        System.out.println(predictTheWinner(new int[] { 1, 5, 233, 7 }));
    }
}