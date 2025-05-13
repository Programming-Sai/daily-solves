
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class ReverseNodesInKGroup {
    static class Segment {
        ListNode newHead;
        ListNode newTail;

        Segment(ListNode h, ListNode t) {
            this.newHead = h;
            this.newTail = t;
        }
    }

    public static ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int length = 0;
        while (curr != null) {
            length++;
            curr = curr.next;
        }

        int numberOfSegments = length / k;

        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        curr = dummy;

        while (curr != null) {
            if (numberOfSegments > 0) {
                Segment seg = reverseList(curr.next, k);
                curr.next = seg.newHead;
                curr = seg.newTail;
                numberOfSegments--;
            }
            // curr = curr.next;
            System.out.println("l");
        }
        return dummy.next;
    }

    public static Segment reverseList(ListNode head, int k) {

        ListNode curr = head;
        ListNode prev = null;
        ListNode nextNode;
        while (curr != null && k > 0) {
            nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
            k--;
        }
        head.next = curr;
        return new Segment(prev, head);
    }

    // Helper to build a list from array
    public static ListNode buildList(int[] values) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (int val : values) {
            current.next = new ListNode(val);
            current = current.next;
        }
        return dummy.next;
    }

    // Helper to print the list
    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + (head.next != null ? " -> " : ""));
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {

        int[] vals1 = { 1, 2, 3, 4, 5 };
        int k1 = 2;
        ListNode head1 = buildList(vals1);
        System.out.print("Original: ");
        printList(head1);
        ListNode result1 = reverseKGroup(head1, k1);
        System.out.print("Reversed (k=" + k1 + "): ");
        printList(result1);

        int[] vals2 = { 1, 2, 3, 4, 5, 6, 7 };
        int k2 = 3;
        ListNode head2 = buildList(vals2);
        System.out.print("Original: ");
        printList(head2);
        ListNode result2 = reverseKGroup(head2, k2);
        System.out.print("Reversed (k=" + k2 + "): ");
        printList(result2);
    }
}
