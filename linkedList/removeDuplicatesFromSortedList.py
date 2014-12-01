class Solution:

    def deleteDuplicates(self,head):
        if head is None:
            return None
        counter = 0
        curr = head
        breakChain = None

        while curr and curr.next is not None:
            prev = curr
            curr = curr.next
            if curr.val == prev.val:
                counter = counter + 1
            else:
                if counter >=1:
                    breakChain.next = curr
                    counter = 0
            if counter == 1:
                breakChain = prev

        if counter >= 1:
            breakChain.next = None

        return head
