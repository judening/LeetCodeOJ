class Solution:
    def exist(self, board, word):
        boardTable = [[False for j in xrange(len(board[0]))] for i in xrange (len(board))]
        if len(word)>len(board)*len(board[0]):
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    boardTable[i][j] = True
                    temp0 = self.loop(board,i,j,word[1:],boardTable)
                    if temp0:
                        return True
                    boardTable[i][j] = False
        return False

    def loop(self,board,row,col,word,boardTable):
        if word == '':
            return True
        else:
            temp0 = None
            temp1 = None
            temp2 = None
            temp3 = None
            if row+1<len(board) and board[row+1][col] == word[0] and boardTable[row+1][col] == False:
                boardTable[row+1][col] = True
                temp0 = self.loop(board,row+1,col,word[1:],boardTable)
                if temp0:
                    return True
                boardTable[row+1][col] = False
            if row-1>=0 and board[row-1][col] == word[0] and boardTable[row-1][col] == False:
                boardTable[row-1][col] = True
                temp1 = self.loop(board,row-1,col,word[1:],boardTable)
                if temp1:
                    return True
                boardTable[row-1][col] = False
            if col+1<len(board[0]) and board[row][col+1] == word[0] and boardTable[row][col+1] == False:
                boardTable[row][col+1] = True
                temp2 = self.loop(board,row,col+1,word[1:],boardTable)
                if temp2:
                    return True
                boardTable[row][col+1] = False
            if col-1>=0 and board[row][col-1] == word[0] and boardTable[row][col-1] == False:
                boardTable[row][col-1] = True
                temp3 = self.loop(board,row,col-1,word[1:],boardTable)
                if temp3:
                    return True
                boardTable[row][col-1] = False
            return False

S = Solution()
testBoard = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
testWord = 'ABCCED'
print S.exist(testBoard,testWord)
