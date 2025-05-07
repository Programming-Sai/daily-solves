import java.util.Stack;

class MinStack {
    Stack<Integer> stack;
    Stack<Integer> monoDecStack;
    // int min;

    public MinStack() {
        stack = new Stack<>();
        monoDecStack = new Stack<>();
        // min = Integer.MAX_VALUE;
    }

    public void push(int val) {
        stack.push(val);
        if (monoDecStack.empty()) {
            monoDecStack.push(val);
        } else if (val < monoDecStack.peek()) {
            monoDecStack.push(val);
        }
        System.out.println(stack + ", " + monoDecStack + ", " + val);
    }

    public void pop() {
        int removed = stack.pop();
        if (removed == monoDecStack.peek()) {
            monoDecStack.pop();
        }

    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        if (monoDecStack.empty()) {
            return stack.peek();
        }
        return monoDecStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */