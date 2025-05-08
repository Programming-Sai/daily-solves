import java.util.Stack;

public class BackspaceStringCompare {
    public static boolean backspaceCompare(String s, String t) {
        Stack<Character> sStack = new Stack<>();
        Stack<Character> tStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (!sStack.isEmpty() && s.charAt(i) == '#') {
                sStack.pop();
            } else if (s.charAt(i) != '#') {
                sStack.push(s.charAt(i));
            }
        }

        for (int j = 0; j < t.length(); j++) {
            if (!tStack.isEmpty() && t.charAt(j) == '#') {
                tStack.pop();
            } else if (t.charAt(j) != '#') {
                tStack.push(t.charAt(j));
            }
        }
        System.out.println(sStack + ", " + tStack);
        return sStack.equals((tStack));
    }

    public static void main(String[] args) {

        // Test Case 1: Basic Matches
        System.out.println(backspaceCompare("ab#c", "ad#c")); // Expected: true
        System.out.println(backspaceCompare("a##c", "#a#c")); // Expected: true
        System.out.println(backspaceCompare("ab##", "c#d#")); // Expected: true

        // Test Case 2: Basic Mismatches
        System.out.println(backspaceCompare("a#c", "b")); // Expected: false
        System.out.println(backspaceCompare("abc#d", "abzz##d")); // Expected: false

        // Test Case 3: Edge Cases
        System.out.println(backspaceCompare("a######", "")); // Expected: true
        System.out.println(backspaceCompare("####", "##")); // Expected: true
        System.out.println(backspaceCompare("", "")); // Expected: true
        System.out.println(backspaceCompare("a#b#c#d#", "####")); // Expected: true

        // Test Case 4: Tricky Ones
        System.out.println(backspaceCompare("bxj##tw", "bxo#j##tw")); // Expected: true
        System.out.println(backspaceCompare("bxj##tw", "bxj###tw")); // Expected: false
    }
}
