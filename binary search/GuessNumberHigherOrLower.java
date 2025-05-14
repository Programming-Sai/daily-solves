
/**
 * Forward declaration of guess API.
 * 
 * @param num your guess
 * @return -1 if num is higher than the picked number
 *         1 if num is lower than the picked number
 *         otherwise return 0
 *         int guess(int num);
 */

public class GuessNumberHigherOrLower {
    public int guessNumber(int n) {
        int l, r, mid, guessNum, res;
        l = 0;
        r = n - 1;
        res = 0;
        while (l <= r) {
            mid = l + (r - l) / 2;
            guessNum = 6;
            // guessNum = guess(mid + 1);f
            if (guessNum == 0) {
                res = mid + 1;
                break;
            } else if (guessNum == -1) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return res;
    }
}
