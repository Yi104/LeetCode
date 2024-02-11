# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Calculate the sum of digits plus carry
            total_sum = carry
            if l1:
                total_sum += l1.val
                l1 = l1.next
            if l2:
                total_sum += l2.val
                l2 = l2.next
            
            # Update carry and create a new node for the result
            carry, digit = divmod(total_sum, 10)
            current.next = ListNode(digit)
            current = current.next
        
        return dummy.next
