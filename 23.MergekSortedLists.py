from queue import PriorityQueue
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min heap
        min_heap = PriorityQueue()

        # Add the first element of each linked list to the heap
        for i, linked_list in enumerate(lists):
            if linked_list:
                min_heap.put((linked_list.val, i, linked_list))

        # Initialize a dummy node to build the merged list
        dummy = ListNode()
        current = dummy

        # Continue until the heap is not empty
        while not min_heap.empty():
            val, i, node = min_heap.get()

            # Add the current node to the merged list
            current.next = node
            current = current.next

            # Move to the next node in the linked list
            if node.next:
                min_heap.put((node.next.val, i, node.next))

        return dummy.next
