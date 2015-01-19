class Solution:
    def spiralOrder(self,matrix):
        toRet = []
        if matrix:
            rowBegin = 0
            rowEnd = len(matrix)-1
            colBegin = 0
            colEnd = len(matrix[0])-1
            while rowBegin<=rowEnd and colBegin<=colEnd:
                for i in xrange(colBegin,colEnd+1):
                    toRet.append(matrix[rowBegin][i])
                rowBegin+=1
                for i in xrange(rowBegin,rowEnd+1):
                    toRet.append(matrix[i][colEnd])
                colEnd-=1
                if rowBegin<=rowEnd:
                    for i in xrange(colEnd,colBegin-1,-1):
                        toRet.append(matrix[rowEnd][i])
                rowEnd -=1
                if colBegin<=colEnd:
                    for i in xrange(rowEnd,rowBegin-1,-1):
                        toRet.append(matrix[i][colBegin])
                colBegin+=1
        return toRet
