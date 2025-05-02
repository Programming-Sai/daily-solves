import java.util.Arrays;
import java.util.Stack;

public class DailyTemperatures {

    public static int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> answerStack = new Stack<>();
        int[] answer = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!answerStack.isEmpty() && temperatures[i] > temperatures[answerStack.peek()]) {
                int last = answerStack.pop();
                answer[last] = i - last;
            }
            answerStack.push(i);
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(dailyTemperatures(new int[] { 73, 74, 75, 71, 69, 72, 76, 73 })));
        // System.out.println(dailyTemperatures(new int[] { 30, 40, 50, 60 }));
        // System.out.println(dailyTemperatures(new int[] { 30, 60, 90 }));
    }
}