# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedLL = ListNode()   
        follower = sortedLL

        currOne, currTwo = list1, list2

        while currOne and currTwo:
            if currOne.val > currTwo.val:
                follower.next = currTwo
                currTwo = currTwo.next
            else:
                follower.next = currOne
                currOne = currOne.next

            follower = follower.next
        if currOne:
            follower.next = currOne
        if currTwo:
            follower.next = currTwo

        return sortedLL.next
