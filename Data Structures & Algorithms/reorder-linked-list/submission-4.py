# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle point to seperate
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        prev = None
        #reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
         
# Time: O(n)
# Three passes, each linear: find middle (~n/2), reverse second half (~n/2),
# merge both halves (~n). Sum of linear passes is still linear.

# Space: O(1)
# Only pointers (slow, fast, prev, first, second, tmp1, tmp2) —
# no extra data structures that scale with inpu

        

