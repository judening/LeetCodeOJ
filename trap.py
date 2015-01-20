class Solution:
    def trap(self,A):
        if not A:
            return 0
        else:
            minimum = A[0]
            miniIndex = 0
            cumulation = 0

            while miniIndex < len(A):
                j = miniIndex+1
                while j<len(A) and A[j]<minimum:
                    j+=1
                if j == len(A):
                    miniIndex +=1
                else:
                    for i in xrange(miniIndex,j):
                        cumulation = cumulation + A[miniIndex]-minimum
                    print minimum
                    minimum = A[j]
                    miniIndex = j
            return cumulation

S = Solution()
print S.trap([0,1,0,2,1,0,1,3,2,1,2,1])
