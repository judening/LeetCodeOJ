class Solution:

    def rotate(self,matrix):
        rotateTimes = len(matrix)/2
        stop = len(matrix)-1

        i = 0
        j = 0

        while i < rotateTimes:
            j = i

            while j < stop:
                # Pay attention here, the offset is distance from
                # j to i. Because of the symetric reason, we should
                # calculate the distance from stop, which is stop-offset
                offset = j-i
                first = matrix[i][j]
                matrix[i][j] = matrix[stop-offset][i]
                matrix[stop-offset][i] = matrix[stop][stop-offset]
                matrix[stop][stop-offset]=matrix[j][stop]
                matrix[j][stop]=first

                j = j+1
            i = i+1
        return matrix
