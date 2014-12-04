class Solution:
    #Recurrsion is so much shorter
    def mergeTwoLists(self,l1,l2):
        newHead = None
        if l1 and l2:
            if l1.val>l2.val:
                newHead = l2
                newHead.next = self.mergeTwoLists(l1,l2.next)
            else:
                newHead = l1
                newHead.next = self.mergeTwoLists(l1.next,l2)
            return newHead
        if not l1 and l2:
            newHead = l2
            return newHead
        if l1 and not l2:
            newHead = l1
            return newHead
