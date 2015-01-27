class Solution:
    def removeDuplicates(self,A):
        n = len(A)
        if n<=2:
            return n
        i,j = 2,2
        while j<n:
            if A[j] != A[i-2]:
                A[i] = A[j]
                i+=1
            j+=1
        return i
