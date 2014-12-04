class Solution:
    #You can't really beat this recurrsion solution. So simple
    def swapPairs(self,head):
        newHead = None
        if head and head.next:
            newHead = head.next
            head.next = self.swapPairs(newHead.next)
            newHead.next = head
            return newHead
        if head and not head.next:
            return head
        return newHead
