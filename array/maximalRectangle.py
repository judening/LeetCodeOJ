class Solution:

    def maxRectangle(self,matrix,row,col):
        minWidth = sys.maxint
        maxArea = 0
        i = row
        while i<len(matrix) and matrix[i][col] == '1':
            width = 0
            while col+width < len(matrix[row]) and matrix[i][col+width] == '1':
                width +=1

            if width<minWidth:
                minWidth = width

            maxArea = max(maxArea, minWidth*(i-row+1))
        return maxArea

    def maximalRectangle(self,matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        maxArea = 0

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    maxArea = max(maxArea,self.maxRectangle(matrix,i,j)

        return maxArea
