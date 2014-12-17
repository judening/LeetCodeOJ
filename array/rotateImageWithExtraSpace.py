class Solution:
    # This way is really trivial
    def rotate(self,matrix):
        n = len(matrix)
        nonInPlace = [[None for i in xrange(n)] for j in xrange(n)]
        for i in xrange(n):
            for j in xrange(n):
                nonInPlace[j][n-1-i] = matrix[i][j]

        return nonInplace
