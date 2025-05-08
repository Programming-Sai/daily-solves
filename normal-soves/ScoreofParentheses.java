import java.util.Stack;

class ScoreofParentheses {
    public static int scoreOfParentheses(String s) {
        Stack<Object> scoreStack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char st = s.charAt(i);
            if (st == '(') {
                scoreStack.push(st);
            } else {
                int sum = 0;
                while (!scoreStack.isEmpty() && scoreStack.peek() instanceof Integer) {
                    sum += (Integer) scoreStack.pop();
                }
                if (!scoreStack.isEmpty() && scoreStack.peek().equals('(')) {
                    scoreStack.pop();
                    scoreStack.push(sum == 0 ? 1 : 2 * sum);
                }
            }
        }
        int result = 0;
        while (!scoreStack.isEmpty()) {
            result += (Integer) scoreStack.pop();
        }
        return result;
    }

    public static void main(String[] args) {

        String[] tests = {
                "()", // Expected: 1
                "(())", // Expected: 2
                "()()", // Expected: 2
                "(()(()))", // Expected: 6
                "((())())", // Expected: 6
                "(((())))", // Expected: 8
                "()(()(()))", // Expected: 7
                "(()()())", // Expected: 6
        };

        for (String test : tests) {
            int result = scoreOfParentheses(test);
            System.out.println("Input: '" + test + "' → Output: " + result);
        }
    }
}