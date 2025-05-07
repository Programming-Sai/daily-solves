
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

public class OddEvenLinkedList {

    public ListNode oddEvenList(ListNode head) {

        ListNode t = head;
        ListNode r = head.next;
        ListNode rh = r;
        while (r != null && r.next != null) {
            t.next = r.next;
            t = t.next;

            r.next = t.next;
            r = r.next;
        }
        t.next = rh;
        return head;
    }

}