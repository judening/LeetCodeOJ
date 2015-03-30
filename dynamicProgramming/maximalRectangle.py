class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self,matrix):
        if len(matrix) ==0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        left = [0 for i in xrange(col)]
        # Height counts the number of successive '1's above
        # Plus the current one
        height = [0 for i in xrange(col)]
        # The value of left and right means the boundaries of the
        # rectangle.
        right = [col for i in xrange(col)]
        maxA = 0
        for i in xrange(row):
            cur_left = 0
            cur_right = col
            for j in xrange(col):
                if matrix[i][j] == '1':
                    height[j] +=1
                else:
                    height[j] = 0
            for j in xrange(col):
                if matrix[i][j] == '1':
                    left[j] = max(left[j],cur_left)
                else:
                    left[j] =0
                    cur_left =j+1
            for j in xrange(col-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = col
                    cur_right = j
            for j in xrange(col):
                maxA = max(maxA,(right[j]-left[j])*height[j])
        return maxA
