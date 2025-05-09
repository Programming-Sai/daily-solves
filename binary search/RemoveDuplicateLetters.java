import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

public class RemoveDuplicateLetters {
    public static String removeDuplicateLetters(String s) {
        HashMap<Character, Integer> lastIndex = new HashMap<>();
        HashSet<Character> seenSet = new HashSet<>();
        Stack<Character> charStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            lastIndex.put(s.charAt(i), i);
        }

        for (int i = 0; i < s.length(); i++) {
            // if (!charStack.isEmpty())
            // System.out.println(i + ", " + lastIndex.get(s.charAt(i)) + ", " + seenSet +
            // ", " + charStack + ", "
            // + s.charAt(i) + ", " + charStack.peek());

            if (seenSet.contains(s.charAt(i))) {
                continue;
            }

            while (!charStack.isEmpty() && i < lastIndex.get(charStack.peek()) && s.charAt(i) < charStack.peek()) {
                seenSet.remove(charStack.pop());
            }
            // if (charStack.isEmpty() || (!seenSet.contains(s.charAt(i)))) {
            charStack.push(s.charAt(i));
            seenSet.add(s.charAt(i));
            // }

        }

        // System.out.println(charStack);

        StringBuilder sb = new StringBuilder();
        for (char c : charStack) {
            sb.append(c);
        }
        String result = sb.toString();

        return result;
    }

    public static void main(String[] args) {
        // Test cases
        System.out.println(removeDuplicateLetters("bcabc")); // Expected output:
        // "abc"
        System.out.println(removeDuplicateLetters("cbacdcbc")); // Expected output:
        // "acdb"
        System.out.println(removeDuplicateLetters("abcdabc")); // Expected output:
        // "abcd"
        System.out.println(removeDuplicateLetters("aabbcc")); // Expected output:
        // "abc"
        System.out.println(removeDuplicateLetters("ecbacba")); // Expected output:
        // "abc"
        System.out.println(removeDuplicateLetters("bbcaac")); // Expected output:
        // "abc"
        System.out.println(removeDuplicateLetters("aaaaaa")); // Expected output: "a"
        System.out.println(removeDuplicateLetters("abacb")); // Expected output: "a"
    }
}
