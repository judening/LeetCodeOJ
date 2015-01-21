class Solution:
    def trap(self,A):
        if not A:
            return 0
        else:
            leftHeightBound = []
            rightHeightBound = []
            leftMax = 0
            rightMax = 0
            totalTrap = 0

            for i in xrange(len(A)):
                if leftMax < A[i]:
                    leftMax = A[i]
                leftHeightBound.append(leftMax)
            for j in xrange(len(A)-1,-1,-1):
                if rightmax < A[i]:
                    rightMax = A[i]
                rightHeightBound.append(rightMax)
            for k in xrange(len(A)):
                if min(leftHeightBound[i],rightHeightBound[i]) > A[i]:
                    totalTrap += min(leftHeightBound[i],rightHeightBound[i]) - A[i]
            return totalTrap
