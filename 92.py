# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node just before the left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Initialize pointers for reversing the sublist
        curr = prev.next
        next_node = curr.next
        
        # Reverse the sublist from left to right
        for _ in range(right - left):
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            next_node = curr.next
        
        return dummy.next
