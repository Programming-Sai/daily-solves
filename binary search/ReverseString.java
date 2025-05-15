public class ReverseString {

    public static char[] rev(char[] s, int l, int r) {
        if (l >= r) {
            return s;
        } else {
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            return rev(s, l + 1, r - 1);
        }
    }

    public static char[] reverseString(char[] s) {
        return rev(s, 0, s.length - 1);
    }

    public static void main(String[] args) {
        System.out.println(reverseString(new char[] { 'h', 'e', 'l', 'l', 'o' }));
        System.out.println(reverseString(new char[] { 'H', 'a', 'n', 'n', 'a', 'h' }));
    }
}