# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:  # Handle empty list case
            return None

        length = self.linkedListLength(head)
        
        # Calculate the middle index.
        # For even length, (length / 2) gives the first of the two middle nodes.
        # For odd length, (length / 2) gives the exact middle node (integer division truncates).
        middle_index = length // 2 
        
        current = head
        for _ in range(middle_index):
            current = current.next
            
        return current

    def linkedListLength(self, head):
        """
        Helper method to calculate the length of the linked list.
        :type head: Optional[ListNode]
        :rtype: int
        """
        length = 0
        current = head  # Start from the head
        while current is not None: # Iterate until current becomes None
            length += 1
            current = current.next
        return length