class Solution:
    def totalNQueens(self,n):
        self.res = []
        arry = [["." for i in xrange(n)] for j in xrange(n)]
        self.helper(arry,0)
        num = len(self.res)
        return num

    def helper(self,arry,row):
        if row == len(arry):
            self.res.append(arry)
            return
        for i in xrange(len(arry)):
            if self.isValid(arry,row,i):
                arry[row][i] = "Q"
                # See the DFS here?
                self.helper(arry,row+1)
                # After you DFS, put back the '.' back to the arry
                arry[row][i] = '.'

    def isValid(self,arry,row,col):
        # Check previous rows
        for i in xrange(row):
            if arry[i][col] == 'Q':
                return False
        tempRow = row -1
        tempCol = col -1
        # Check left previous diagonal
        while tempRow >=0 and tempCol>=0:
            if arry[tempRow][tempCol] == 'Q':
                return False
            tempRow = tempRow-1
            tempCol = tempCol-1
        tempRow = row-1
        tempCol = col+1 #This is on the right, that's why col = col+1
        # Check right previous diagonal
        while tempRow>=0 and tempCol < len(arry):
            if arry[tempRow][tempCol] == 'Q':
                return False
            tempRow = tempRow-1
            tempCol = tempCol+1
        return True
