import java.util.Stack;

public class SumofSubarrayMinimums {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        Stack<Integer> stackOne = new Stack<>();
        Stack<Integer> stackTwo = new Stack<>();
        int[] left = new int[n];
        int[] right = new int[n];
        int MOD = (int) 1e9 + 7;

        // Left pass (Previous Less)
        for (int i = 0; i < n; i++) {
            while (!stackOne.isEmpty() && arr[stackOne.peek()] > arr[i]) {
                stackOne.pop();
            }

            left[i] = stackOne.isEmpty() ? i + 1 : i - stackOne.peek();
            stackOne.push(i);
        }

        // Right pass (Next Less or Equal)
        for (int i = n - 1; i >= 0; i--) {
            while (!stackTwo.isEmpty() && arr[stackTwo.peek()] >= arr[i]) {
                stackTwo.pop();
            }

            right[i] = stackTwo.isEmpty() ? n - i : stackTwo.peek() - i;
            stackTwo.push(i);
        }

        long result = 0;
        for (int i = 0; i < n; i++) {
            result = (result + (long) arr[i] * left[i] * right[i]) % MOD;
        }
        return (int) result;
    }

    public static void main(String[] args) {
        SumofSubarrayMinimums solver = new SumofSubarrayMinimums();

        int[] arr1 = { 3, 1, 2, 4 };
        int[] arr2 = { 11, 81, 94, 43, 3 };
        int[] arr3 = { 1, 2, 3, 4, 5 };

        System.out.println("Result 1: " + solver.sumSubarrayMins(arr1)); // Expected: 17
        System.out.println("Result 2: " + solver.sumSubarrayMins(arr2)); // Expected: 444
        System.out.println("Result 3: " + solver.sumSubarrayMins(arr3)); // Optional test
    }
}
