import java.util.Stack;

public class CrawlerLogFolder {
    public int minOperations(String[] logs) {
        Stack<String> fileStack = new Stack<>();

        for (String log : logs) {
            if (log.equals("../") && !fileStack.empty()) {
                fileStack.pop();
            } else if (log.equals("./")) {
            } else {
                fileStack.push(log);
            }
            System.out.println(fileStack);
        }
        return fileStack.size();
    }
}
