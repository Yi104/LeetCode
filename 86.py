# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Initialize two dummy nodes to keep track of elements less than x and elements greater or equal to x
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head
        
        # Traverse through the original list
        while head:
            # If the current node's value is less than x, append it to the "before" list
            if head.val < x:
                before.next = head
                before = before.next
            # If the current node's value is greater or equal to x, append it to the "after" list
            else:
                after.next = head
                after = after.next
            head = head.next
        
        # Connect the "before" list with the "after" list
        after.next = None
        before.next = after_head.next
        
        # Return the head of the "before" list
        return before_head.next
