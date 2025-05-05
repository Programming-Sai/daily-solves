public class LongestSubarraywithSumK {

    public static int longestSubarraywithSumK(int[] arr, int k) {
        int l = 0, length = 0, curr_sum = 0;
        for (int r = 0; r < arr.length; r++) {
            curr_sum += arr[r];
            while (curr_sum > k && l < arr.length) {
                curr_sum -= arr[l];
                l += 1;
            }
            length = Math.max(length, (r - l + 1));
        }
        return length;
    }

    public static void main(String[] args) {
        int[] arr = new int[] { 1, 2, 1, 0, 1, 1, 0 };
        int k = 4;

        System.out.println(longestSubarraywithSumK(arr, k));

    }
}