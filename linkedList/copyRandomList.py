class Solution:
    #So the critical point of this problem is to have a hash table to
    #store the existing nodes such that you don't create a duplicate "object"
    def copyRnadomList(self,head):
        existNode = {}
        newHead = None
        if not head:
            return newHead
        newHead = RandomListNode(head.label)
        existNode[head.label] = newHead

        iterv = head
        curr = newHead
        while iterv:
            if iterv.next:
                newNext = None
                if not existNode.get(iterv.next.label):
                    existNode[iterv.next.label] = newNext
                else:
                    newNext = existNode[iterv.next.label]
                curr.next = newNext
            if iterv.random:
                newRandom = None
                if not existNode.get(iterv.random.label):
                    newRandom = RndomListNode(iterv.random.label)
                    existNode[iterv.random.label] = newRandom
                else:
                    newRandom = existNode[iterv.random.label]
                curr.random = newRandom
            iterv = iterv.next
            curr = curr.next

        return newHead
