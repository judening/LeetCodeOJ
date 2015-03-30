class Solution:
    # Let's do this by finding the maxiaml area
    # that *one point can constitue as a rectangle first
    def maxRectangle(self,matrix,row,col):
        minWidth = sys.maxint
        maxArea = 0
        i = row
        # Step 1. Make sure the starting point is a "1"
        while i<len(matrix) and matrix[i][col] == '1':
            width = 0
            # Step 2. Check how many 1 is in each row
            # This constitues the width
            while col+width < len(matrix[row]) and matrix[i][col+width] == '1':
                width +=1

            # Step 3. Compare the widths
            # The mini width is the constrain of the area of this rectangle
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
                    # Go thru each point in the matrix
                    maxArea = max(maxArea,self.maxRectangle(matrix,i,j)

        return maxArea
