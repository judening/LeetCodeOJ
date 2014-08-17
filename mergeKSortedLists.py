class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self,lists):
        newHead = None

        if len(lists) == 0:
            return None

        elif len(lists) == 1:
            return lists[0]

        elif len(lists)>1:
            for head in lists:
                if head is None:
                    lists.remove(head)

            newHead = lists[0]
            for i in range(1,len(lists)):
                sortedHead = lists[i]
                iterPrev = None
                iterHead = newHead
                while sortedHead is not None and iterHead is not None:
                    if sortedHead.val <= iterHead.val:
                        temp = sortedHead.next
                        sortedHead.next = iterHead

                        if iterPrev is None:
                            newHead = sortedHead
                        else:
                            iterPrev.next = sortedHead

                        iterPrev = sortedHead
                        sortedHead = temp
                    else:
                        iterPrev = iterHead
                        iterHead = iterHead.next
                        iterNone = True

                        while iterHead is not None:
                            print "I should be able to see -2 here, right?" , sortedHead.val
                            if sortedHead.val <= iterHead.val:
                                print iterPrev.val
                                iterPrev.next = sortedHead
                                temp = sortedHead.next
                                sortedHead.next = iterHead
                                sortedHead = temp
                                iterNone = False
                                break
                            else:
                                iterPrev = iterHead
                                iterHead = iterHead.next

                        if iterNone:
                            iterPrev.next = sortedHead
                            sortedHead.next = iterHead
                            break
            return newHead

Head = ListNode(-1)
a = ListNode(1)
Head.next = a

Head_1 = ListNode(-3)
b = ListNode(1)
c = ListNode(4)

Head_1.next = b
b.next = c

Head_2 = ListNode(-2)
h = ListNode(-1)
i = ListNode(0)
j = ListNode(2)

Head_2.next = h
h.next = i
i.next = j

Head_3 = ListNode(-2)
k = ListNode(6)
l = ListNode(7)
Head_3.next = k
k.next = l
f = [Head,Head_1,Head_2,Head_3]
e = Solution()
g = e.mergeKLists(f)

print "Print out the list here."
while g is not None:
    print g.val
    g = g.next
