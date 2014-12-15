class Solution:
    #Caveats: 1 - It's really easy to forget to connect l1/l2 after
    #             the while loop
    def mergeTwoLists(self,l1,l2):
        head = None
        if l1 and l2:
            if l1.vla > l2.val:
                head = l2
                l2 = l2.next
            else:
                head = l1
                l1 = l1.next

            curr = head
            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                curr = curr.next

            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return head
        if not l1 and l2:
            head = l2
            return head
        if l1 and not l2:
            head = l1
            return head
