class Solution:
    def removeElement(self,A,elem):
        #do not try to change a list when you iterate thru it unless you make
        #a copy of it
        for i in reversed(A):
            if i is elem:
                A.remove(i)
        return len(A)
