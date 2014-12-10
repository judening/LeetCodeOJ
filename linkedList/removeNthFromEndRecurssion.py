class Solution
    #Isn't recurssion beautiful?
    def removeNthFromEnd(self,head,n):
        self.nthPre = None
        self.nthNext = None
        curr = head
        self.removeHthHelper(head,0,n)
        if self.nthPre:
            self.nthPre.next = self.nthNext
        else:
            head = self.nthNext

        return head
    def removeNthHelper(self,curr,temp,n):
        if not curr:
            return 0
        else:
            temp = self.removeNthHelper(curr.next,temp,n)+1
            if temp == n-1:
                self.nthNext = curr
            if temp == n+1:
                self.nthPre = curr
            return temp
