import java.util.ArrayList;
import java.util.List;

public class PascalsTriangleII {
    public static List<Integer> getRow(int rowIndex) {
        long prev = 1;
        List<Integer> tri = new ArrayList<>();
        for (int i = 0; i <= rowIndex; i++) {
            if (i == 0) {
                tri.add(1);
            } else {
                prev = prev * (rowIndex - i + 1) / i;
                tri.add((int) prev);
            }
        }
        return tri;
    }

    public static void main(String[] args) {
        System.out.println(getRow(0));
        System.out.println(getRow(1));
        System.out.println(getRow(2));
        System.out.println(getRow(3));
        System.out.println(getRow(4));
        System.out.println(getRow(5));
        System.out.println(getRow(33));
    }
}
