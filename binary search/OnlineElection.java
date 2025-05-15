import java.util.HashMap;

public class OnlineElection {
    static class TopVotedCandidate {
        private int[] leaders, times;
        private int n;

        public TopVotedCandidate(int[] persons, int[] times) {
            int n, maxVotes, currentLeader;
            this.n = persons.length;
            maxVotes = 0;
            currentLeader = 0;
            HashMap<Integer, Integer> votes = new HashMap<>();
            int[] leaders = new int[this.n];
            for (int i = 0; i < this.n; i += 1) {
                votes.put(persons[i], votes.getOrDefault(persons[i], 0) + 1);
                if (votes.get(persons[i]) >= maxVotes) {
                    maxVotes = votes.get(persons[i]);
                    currentLeader = persons[i];
                    leaders[i] = currentLeader;
                }
                leaders[i] = currentLeader;
            }
            this.leaders = leaders;
            this.times = times;
        }

        public int binSearch(int t) {
            int l, r, mid;
            l = 0;
            r = this.n - 1;
            while (l <= r) {
                mid = l + (r - l) / 2;
                if (this.times[mid] == t) {
                    return mid;
                } else if (this.times[mid] > t) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
            return r;
        }

        public int q(int t) {
            int idx = this.binSearch(t);
            return this.leaders[idx];
        }
    }

    public static void main(String[] args) {
        // TopVotedCandidate k = new TopVotedCandidate(new int[] { 0, 1, 1, 0, 0, 1, 0
        // },
        // new int[] { 0, 5, 10, 15, 20, 25, 30 });
        // System.out.print(
        // "[ " +
        // k.q(3) + ", " +
        // k.q(12) + ", " +
        // k.q(25) + ", " +
        // k.q(15) + ", " +
        // k.q(24) + ", " +
        // k.q(8) + " ]");
        // }

        TopVotedCandidate k = new TopVotedCandidate(new int[] { 0, 0, 1, 1, 2 },
                new int[] { 0, 67, 69, 74, 87 });
        System.out.print(
                "[ " +
                        k.q(4) + ", " +
                        k.q(62) + ", " +
                        k.q(100) + ", " +
                        k.q(88) + ", " +
                        k.q(70) + ", " +
                        k.q(73) + ", " +
                        k.q(22) + ", " +
                        k.q(75) + ", " +
                        k.q(29) + ", " +
                        k.q(10) + " ]");
    }
}
