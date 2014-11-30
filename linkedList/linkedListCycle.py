class Solution:
    #Imagin there are two persons racing and they run round the loop.
    #The faster one will eventually meet up with the slower one since
    #IT IS A LOOP!!!!
    def hasCycle(self,head):
        slow = head
        fast = head
        if head is None:
            return False
        while not (fast is None) and not (fast.next is None):
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
