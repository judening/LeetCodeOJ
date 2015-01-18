class Solution:
    def reverseKGroup(self,head,k):
        curr = head
        count = 0
        while curr and count!=k:
            curr = curr.next
            count +=1
        if count == k
            # Reverse the next k nodes first
            curr = self.reverseKGroup(curr,k)
            while count>0:
                # The logic here is always to connect the head
                # of first K nodes with next K nodes (which has been reversed)
                # then for the first k nodes, reverse it one by one
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                count -=1
            head = curr
        return head

