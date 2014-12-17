class Solution:
    # Typical DB problem
    # 1. Create a new variable to store results
    # 2. Initialize the table when row = 0 || column =0
    # 3. Fill in the table
    # For this problem, just think twice before what to fill in the minGrid
    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])
        minGrid = [[None for i in xrange(n)] for j in xrange(m)]
        last = 0
        for i in xrange(n):
            minGrid[0][i] = last + grid[0][i]
            last = minGrid[0][i]

        for j in xrange(m):
            minGrid[j][0] = last + grid[j][0]

        for i in xrange(1,m):
            for j in xrange(1,n):
                minGrid[i][j] = grid[i][j] + min(minGrid[i-1][j],minGrid[i][j-1])

        return minGrid[m-1][n-1]
