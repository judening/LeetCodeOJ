class Solution:

    def removeElement(self,A,elem):
        start = 0
        end = len(A)-1
        while start<= end:
            while start < len(A) and A[start] != elem:
                start = start + 1
            while end >=0 and A[end] == elem:
                end = end-1

            if start<=end:
                A[start],A[end] = A[end],A[start]
        return start
