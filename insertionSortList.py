# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        newHead = head
        if head is not None:
            newHead.next = None
            while head.next is not None:
                head = head.next
                if head.val <= newHead.val:
                    head, newHead = newHead, head
                    newHead.next = head
                else:
                    tmp = newHead
                    while tmp.next is not None:
                        prev = tmp
                        tmp = tmp.next
                        if head.val <= tmp.val and head.val > prev.val:
                            prev , head = prev, head
                            prev.next = head
                            head.next = tmp
                    if tmp.next == null and head.val > tmp.val:
                        tmp.next = head
                        head.next = null
                
            return newHead
        else:
            return head
