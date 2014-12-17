class Solution:

    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if i==0 and j!=0 :
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif i!=0 and j==0 :
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif i==0 and j==0 :
                    grid[i][j] = grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]
        return grid[m-1][n-1]
