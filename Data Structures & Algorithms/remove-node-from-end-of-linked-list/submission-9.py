# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        ahead = before = dummy
        dummy.next = head

        for _ in range(n+1):
            ahead= ahead.next
        while ahead:
            ahead = ahead.next
            before = before.next
        before.next = before.next.next
        return dummy.next

# Time: O(L)  where L = length of the list. 
# Space: O(1)