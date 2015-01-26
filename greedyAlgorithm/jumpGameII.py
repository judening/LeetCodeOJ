class Solution:
    def jump(self,A):
        lastMax = 0
        minStep = 0
        m = 0

        for i in xrange(len(A)):
            # LastMax to record the maximum steps that each index could get
            if i > lastMax:
                # So only when i > lastMax, we need to step forward
                lastMax = m
                minStep = minStep + 1
            m = max(A[i]+i,m)
        return minStep
