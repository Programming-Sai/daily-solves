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

public class MiddleoftheLinkedList {
    public ListNode middleNode(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode t = head, r = head;
        while (r != null && r.next != null) {
            t = t.next;
            r = r.next.next;
        }
        return t;
    }
}
