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

public class LinkedListCycleII {
    public static ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }

        ListNode t = head, r = head;
        while (r != null && r.next != null) {
            t = t.next;
            r = r.next.next;
            if (r == t) {
                break;
            }
        }
        if (r == null && r.next == null) {
            return null;
        }

        t = head;
        while (r != t) {
            t = t.next;
            r = r.next;
        }
        return t;
    }

    public static void main(String[] args) {
        // [3,2,0,-4]
        ListNode head = new ListNode(3, new ListNode(2));
        ListNode cy = head.next;
        head.next.next = new ListNode(0, new ListNode(-4, cy));

        System.out.println(detectCycle(head).val);
    }
}
