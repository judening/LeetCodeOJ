class Solution:
    # This way is really trivial
    def rotate(self,matrix):
        nonInPlace = [[] for j in xrange(n)]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix)):
                nonInPlace[j].insert(0,matrix[i][j])
        return nonInplace
