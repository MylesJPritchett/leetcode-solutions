# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        multi = 1
        while l1:
            total = total + (multi * l1.val)
            l1 = l1.next
            multi = multi * 10
        
        print(total)
        multi = 1
        while l2:
            total = total + (multi * l2.val)
            l2 = l2.next
            multi = multi * 10
            
        print(total)
        
        digits = [int(x) for x in str(total)]
        cur = dummy = ListNode(0)
        for digit in digits[::-1]:
            cur.next = ListNode(digit)
            cur = cur.next
           
        return dummy.next
            