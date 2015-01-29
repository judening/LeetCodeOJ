class Solution:
    def firstMissingPositive(self,A):
        i = 0
        n = len(A)
        while i<n:
            # Index i is where i+1 supposed to be in
            # For the continuous positive array,
            # It's supposed to be greater than 0 and smaller than
            # the size of length
            # The last one is probably the most important
            # It checks if where A[i] supposed to be is in the place
            # Not only it checks for duplicate, it helps identify where we want
            # to move
            if A[i] != i+1 and A[i]>=1 and A[i]<= n and A[A[i]-1] != A[i]:
                temp = A[i]
                A[i] = A[temp-1]
                A[temp-1] = temp
            else:
                i+=1
        for i in xrange(n):
            if A[i] != i+1:
                return i+1
        # The last one pretty much make sure that this array is an array starting with one
        # also, the missing positive is the last one
        return n +1

S = Solution()
print S.firstMissingPositive([2,1])
