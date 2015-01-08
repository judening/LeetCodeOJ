class Solution:

    def isValidSudoku(self,board):

        # check row
        for row in board:
            dup = []
            for i in row:
                if i != '.':
                    if i not in dup:
                        dup.append(i)
                    else:
                        return False

        # check col
        for i in xrange(9):
            dup = []
            for j in xrange(9):
                k = board[j][i]
                if k!= '.':
                    if k not in dup:
                        dup.append(k)
                    else:
                        return False

        # check clusters
        for i in [0,3,6]:
            for j in [0,3,6]:
                dup = []
                for m in xrange(3):
                    for n in xrange(3):
                        k = board[i+m][j+n]
                        if k != '.':
                            if k not in dup:
                                dup.append(k)
                            else:
                                return False

        return True

