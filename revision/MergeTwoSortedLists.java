public class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode sortedLL = new ListNode();
        ListNode follower = sortedLL;

        ListNode currOne = list1, currTwo = list2;

        while (currOne != null && currTwo != null){
            if (currOne.val > currTwo.val){
                follower.next = currTwo;
                currTwo = currTwo.next;
            }else {
                follower.next = currOne;
                currOne = currOne.next;
            }
            follower = follower.next;
        }

        if (follower != null){
            if (currOne != null){
                follower.next = currOne;
            }
            if (currTwo != null){
                follower.next = currTwo;
            }
        }
        return sortedLL.next;
    }
    
}
