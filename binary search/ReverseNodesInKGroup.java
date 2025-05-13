
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
    public static ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode curr = dummy;

        while (curr != null) {
            ListNode segTail = curr;
            if (curr.next != null) {
                segTail.next = reverseList(curr.next);
            }
            curr = curr.next;
        }

    }

    public static ListNode reverseList(ListNode head) {

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
