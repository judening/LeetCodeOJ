class Solution:

    def totalNQueens(self, n):
        self.res = []
        arry = []
        self.helper(arry,0)
        num = len(self.res)
        return num

    def helper(self,arry,row):
        if row == len(arry):
            self.res.append(arry)
            return

        for i in range(len(arry)):
            if self.isValid(arry,row,i):
                arry[row][i] = 'Q'
                self.helper(arry,row+1)
                arry[row][col] = '.'


    def isValid(self,arry,row,col):
        #Check rows
        for i in range(row):
            if arry[i][col] == 'Q':
                return False
        tempRow = row-1
        tempCol = col-1

        #Check left diagonal
        while tempRow >= 0 and tempCol >= 0:
            if arry[tempRow][tempCol] == 'Q':
                return False
            tempRow = tempRow - 1
            tempCol = tempCol - 1

        tempRow = row-1
        tempCol = col+1

        #Check right diagonal
        while tempRow >= 0 and tempCol < len(arry):
            if arry[tempRow][tempCol] == 'Q':
                return False
            tempRow = tempRow - 1
            tempCol = tempCol + 1

        return True

