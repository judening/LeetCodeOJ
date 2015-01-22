class Solution:
    def setZeroes(self,matrix):
        leadingNum = 1
        leadingCol = 1
        leadingRow = 1
        if matrix[0][0] == 0:
            leadingNum = 0
        for i in xrange(1,len(matrix)):
            if matrix[i][0] == 0:
                leadingCol = 0
        for j in xrange(1,len(matrix[0])):
            if matrix[0][j] == 0:
                leadingRow = 0
        for i in xrange(1,len(matrix)):
            for j in xrange(1,len(matrix)):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in xrange(1,len(matrix)):
            for j in xrange(1,len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if leadingCol == 0:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0
        if leadingRow == 0:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0

        if leadingNum == 0
            for i in xrange(len(matrix)):
                matrix[i][0] = 0
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0
        return
