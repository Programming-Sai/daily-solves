public class FindSmallestLetterGreaterThanTarget {
    public char nextGreatestLetter(char[] letters, char target) {
        int l, r, mid, ans;
        l = 0;
        r = letters.length - 1;
        ans = -1;
        while (l <= r) {
            mid = l + (r - l) / 2;
            if (letters[mid] > target) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        if (ans == -1) {
            return letters[0];
        } else {
            return letters[ans];
        }
    }

}
