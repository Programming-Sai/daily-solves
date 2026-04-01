# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow, isCycle = head, head, False
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
            if slow == fast:
                isCycle = True
                break
        if not isCycle: return None
        fast = head
        while fast:
            if fast == slow: return fast
            fast = fast.next
            slow = slow.next
