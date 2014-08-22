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

            z = lists[0]
            for i in range(1,len(lists)):
                y = lists[i]
                z = self.mergeTwoList(z,y)
        return z


    def mergeTwoList(self,list1,list2):
        head = None
        cur = None
        next1 = None
        next2 = None
        if list1.val <= list2.val:
            cur = list1
            next1 = cur.next
            next2 = list2
        else:
            cur = list2
            next1 =cur.next
            next2 = list1

        head = cur
        while next1 and next2:
            if next1.val <= next2.val:
                cur.next = next1
                cur = next1
                next1 = next1.next
            else:
                cur.next = next2
                cur = next2
                next2 = next2.next
        if next1:
            cur.next = next1
        else:
            cur.next = next2

        return head

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

Head_4 = ListNode(None)
f = [Head,Head_1,Head_2,Head_3,Head_4]
e = Solution()
g = e.mergeKLists(f)

