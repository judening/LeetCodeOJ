class Solution:
    def uniquePaths(self,obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid:
            dp = [[None for i in xrange(n)] for j in xrange(m)]
            if m*n == 1:
                return abs(obstacleGrid[0][0]-1)
            else:
                if obstacleGrid[0][0] == 0:
                    dp[0][0] = 1
                else:
                    dp[0][0] = 0

            for i in xrange(1,n):
                if obstacleGrid[0][i] == 0 and dp[0][i-1] ==1:
                    dp[0][i] = 1
                else:
                    dp[0][i] = 0

            for j in xrange(1,m):
                if obstacleGrid[j][0] == 0 and dp[j-1][0] ==1:
                    dp[j][0] = 1
                else:
                    dp[j][0] = 0

            for i in xrange(1,m):
                for j in xrange(1,n):
                    if obstacleGrid[i][j] == 0:
                        dp[i][j] = dp[i-1][j] +dp[i][j-1]
                    else:
                        dp[i][j] = 0

            return dp[m-1][n-1]
