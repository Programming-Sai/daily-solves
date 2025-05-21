public class CountGoodNumbers {
    public static int countGoodNumbers(long n) {
        long evenCount, primeCount;
        evenCount = (n + 1) / 2;
        primeCount = (n) / 2;

        return (int) ((modExpo(5, evenCount, 1_000_000_007) * modExpo(4, primeCount, 1_000_000_007)) % 1_000_000_007);
    }

    static long modExpo(long a, long b, int m) {
        if (b == 0)
            return 1;

        long half = modExpo(a, b / 2, m);
        half = (half * half) % m;
        if (b % 2 == 1) {
            half = (half * a) % m;
        }
        return half;
    }

    public static void main(String[] args) {
        System.out.println(countGoodNumbers((1)));
        System.out.println(countGoodNumbers((4)));
        System.out.println(countGoodNumbers((50)));
    }
}
