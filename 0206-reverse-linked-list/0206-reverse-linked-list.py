# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        # iterative = T O(n), M(1) using 2 pointers
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
        # recursive = T O(n), M(n)
        
        if not head:
            return None
        
        newHead = head
        if head.next:
            newhead= self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
            