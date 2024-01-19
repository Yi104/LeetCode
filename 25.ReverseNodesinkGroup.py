# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(head, k):
            count = 0
            current = head
            
            # Count the number of nodes in the current k-group
            while current and count < k:
                current = current.next
                count += 1
            
            # If there are enough nodes for a k-group, reverse them
            if count == k:
                # Reverse the first k nodes
                reversed_head = self.reverse_list(head, k)
                
                # Recursively reverse the remaining nodes
                head.next = self.reverseKGroup(current, k)
                
                return reversed_head
            
            # If there are less than k nodes, return the original head
            return head
        
        def reverse_list(head, k):
            prev = None
            current = head
            
            # Reverse the first k nodes
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            return prev
        
        # Start the recursion
        return reverse_list(head, k)
