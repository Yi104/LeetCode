class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or k == 0:
        return head
    
    # Calculate the length of the list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1
    
    # Connect the last node to the head to make it a circular list
    current.next = head
    
    # Calculate the actual rotation amount
    k = k % length
    
    # Find the new tail which is at position (length - k - 1)
    new_tail_position = length - k - 1
    new_tail = head
    for _ in range(new_tail_position):
        new_tail = new_tail.next
    
    # Update the new head and break the circular connection
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head
