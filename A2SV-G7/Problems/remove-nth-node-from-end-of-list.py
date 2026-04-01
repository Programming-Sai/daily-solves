# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        if n == count: return head.next
        nth_from_end = count - n + 1
        curr = head
        while curr:
            print(nth_from_end)
            if curr.next and nth_from_end == 2:
                curr.next = curr.next.next
                break
            nth_from_end -= 1
            curr = curr.next
        return head
        
