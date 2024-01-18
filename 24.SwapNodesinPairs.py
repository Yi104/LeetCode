# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Initialize pointers for swapping
        prev = None
        curr = head
        
        # Traverse the list and swap pairs
        while curr and curr.next:
            # Nodes to be swapped
            first_node = curr
            second_node = curr.next
            
            # Update pointers for next iteration
            curr = second_node.next
            if prev:
                prev.next = second_node
            else:
                head = second_node
            
            # Perform the swap
            second_node.next = first_node
            first_node.next = curr
            
            # Update the previous pointer for the next iteration
            prev = first_node
        
        return head
