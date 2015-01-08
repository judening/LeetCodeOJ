class Solution:
    # IT'S ACTUALLY DFS gosh
    # This is a pretty standard DFS
    def solveSudoku(self,board):
        self.solving(board,0)

    def solving(self,board,num):
        if num == 81:
            return True
        else:
            #Remind me of a question asking to do a binary search in a matrix
            row = num/9
            col = num%9
            if board[row][col] != '.':
                return self.solving(board,num+1)
            else:
                for i in xrange(1,10):
                    if not (self.isInRow(board,row,i) or self.isInCol(board,col,i) or self.isInBox(board,row,col,i)):
                        board[row][col] = str(i)
                        if self.solving(board,num+1):
                            return True
                        else:
                            board[row][col] = '.'
                return False

    def isInRow(self,board,row,char):
        for i in xrange(9):
            if board[row][i] == str(char):
                return True
        return False

    def isInCol(self,board,col,char):
        for i in xrange(9):
            if board[i][col] == str(char):
                return True
        return False

    def isInBox(self,board,row,col,char):
        boxRow = row/3
        boxCol = col/3
        for i in xrange(3*boxRow,3*boxRow+1):
            for j in xrange(3*boxCol,3*boxCol+1):
                if board[i][j] == str(char):
                    return True
        return False
