class Solution:

    def sortColors(self,A):
        i,j,k = -1,-1,-1
        for p in xrange(len(A)):
            if A[p] == 0:
                k = k+1
                j = j+1
                i = i+1
                A[k] = 2
                A[j] = 1
                A[i] = 0
            elif A[p] == 1:
                k = k+1
                j = j+1
                A[k] = 2
                A[j] = 1
            else:
                k = k+1
                A[k] = 2
