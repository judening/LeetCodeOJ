class Solution:
    def removeNthFromEnd(self,head,n):
        p1 = head
        for i in xrange(n-1):
            if p1.next is None:
                return
            p1 = p1.next
        if p1.next is None:
            head = head.next
            return head
        else:
            p1 = p1.next
            p2 = head
            while p1.next is not None:
                p1 = p1.next
                p2 = p2.next
            p2.next = p2.next.next
            return head
