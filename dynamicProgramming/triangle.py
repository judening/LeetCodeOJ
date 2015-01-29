class Solution:
    def minimumTotal(self,triangle):
        for i in reversed(xrange(len(triangle) - 1)):
            for j in xrange(0,i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
