import java.util.ArrayList;
import java.util.Stack;

public class CarFleet {

    public static int carFleet(int target, int[] position, int[] speed) {
        Stack<Double> fleetStack = new Stack<>();
        ArrayList<int[]> cars = new ArrayList<>();

        for (int i = 0; i < position.length; i++) {
            cars.add(new int[] { position[i], speed[i] });
        }

        cars.sort((a, b) -> Integer.compare(b[0], a[0]));

        for (int j = 0; j < cars.size(); j++) {
            double time = (target - cars.get(j)[0]) / (double) cars.get(j)[1];
            if (fleetStack.isEmpty() || time > fleetStack.peek()) {
                fleetStack.push(time);
            }
        }
        return fleetStack.size();
    }

    public static void main(String[] args) {
        System.out.println(carFleet(12, new int[] { 10, 8, 0, 5, 3 }, new int[] { 2, 4, 1, 1, 3 })); // ➜ 3
        System.out.println(carFleet(10, new int[] { 3 }, new int[] { 3 })); // ➜ 1
        System.out.println(carFleet(100, new int[] { 0, 2, 4 }, new int[] { 4, 2, 1 })); // ➜ 1

        System.out.println(carFleet(10, new int[] { 0, 2, 4 }, new int[] { 4, 4, 4 })); // ➜ 3
        // // All same speed, no one catches up.

        System.out.println(carFleet(10, new int[] { 6, 8 }, new int[] { 3, 2 })); //
        System.out.println(carFleet(10, new int[] { 0, 4, 2 }, new int[] { 2, 1, 3 })); //
        // ➜ 2
        // // Slower car in front, faster car behind, but not enough distance to catch.

        // System.out.println(carFleet(15, new int[] { 3, 6, 9 }, new int[] { 3, 2, 1
        // })); // ➜ 1
        // // Classic merging chain reaction.

        // System.out.println(carFleet(20, new int[] { 5, 10, 15 }, new int[] { 1, 1, 1
        // })); // ➜ 3
        // All too far apart, same speed — never merge.

    }

}