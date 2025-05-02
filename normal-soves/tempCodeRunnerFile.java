        Stack<Integer> answerStack = new Stack<>();
        int[] answer = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!answerStack.isEmpty() && temperatures[i] > temperatures[answerStack.peek()]) {
                answerStack.pop();
            }
            answerStack.push(i);
            answer[i] = answerStack.peek() - i;
            System.out.println(answerStack);
            // System.out.println(Arrays.toString(answer)); // Option 3
        }

        return answer;