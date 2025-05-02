import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class DailyTemperatures {

    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> answerStack = new Stack<>();
        ArrayList<Integer> answer = new ArrayList<>();

        for (int temp : temperatures) {
            while (!answerStack.isEmpty() && temp <= answerStack.peek()) {
                answerStack.pop();
            }
            answerStack.push(temp);
            Integer[] stackArray = answerStack.toArray(new Integer[0]);
            System.out.println(Arrays.toString(stackArray));

        }

        return new int[] {};
    }

    public static void main(String[] args) {
        System.out.println(new int[] { 73, 74, 75, 71, 69, 72, 76, 73 });
        // System.out.println(new int[] { 30, 40, 50, 60 });
        // System.out.println(new int[] { 30, 60, 90 });
    }
}