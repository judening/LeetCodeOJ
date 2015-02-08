class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        toRet = [[None for i in xrange(n)] for j in xrange(n)]
        rowBegin = 0
        rowEnd = n-1
        colBegin = 0
        colEnd = n-1
        counter = 1
        while rowBegin <= rowEnd and colBegin <=colEnd:
            for i in xrange(colBegin,colEnd+1):
                toRet[rowBegin][i] = counter
                counter +=1
            rowBegin +=1
            for i in xrange(rowBegin,rowEnd+1):
                toRet[i][colEnd] = counter
                counter +=1
            colEnd -=1
            if rowBegin <=rowEnd:
                for i in xrange(colEnd,colBegin-1,-1):
                    toRet[rowEnd][i] = counter
                    counter+=1
            rowEnd-=1
            if colBegin<=colEnd:
                for i in xrange(rowEnd,rowBegin-1,-1):
                    toRet[i][colBegin] = counter
                    counter+=1
            colBegin+=1
        return toRet
