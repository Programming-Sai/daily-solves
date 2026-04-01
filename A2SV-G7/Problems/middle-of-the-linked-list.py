# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        mid = (count // 2) + 1
        print(mid)
        mid_node = None
        curr = head
        while curr:
            print(curr.val)
            if mid == 1:
                return curr
            curr = curr.next
            mid -= 1
