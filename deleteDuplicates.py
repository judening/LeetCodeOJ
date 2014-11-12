# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        newHead = head
        tmp = newHead
        
        if head is None:
            return None
        
        while head is not None:
            head = head.next
            if head is not None:
                if head.val !=tmp.val:
                    tmp.next = head
                    tmp = tmp.next
        
        
        return newHead
        
        
