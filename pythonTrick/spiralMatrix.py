class Solution:

    def spiralOrder(self,matrix):
        if matrix:
            matrixCopy = list(matrix)
            toRet = []

            while matrixCopy:
                n = len(matrixCopy[0])
                i = 0
                while i < n:
                    toRet.append(matrixCopy[0][i])
                    i +=1
                del matrixCopy[0]
                print matrixCopy
                if not matrixCopy:
                    break

                m = len(matrixCopy)
                j = 0
                while j < m:
                    toRet.append(matrixCopy[j][-1])
                    del matrixCopy[j][-1]
                    j +=1
                if not matrixCopy or not matrixCopy[0]:
                    break

                n = len(matrixCopy[0])
                i = n-1
                while i>=0:
                    toRet.append(matrixCopy[-1][i])
                    i -=1
                print matrixCopy
                if not matrixCopy:
                    break

                m = len(matrixCopy)
                j = m-1
                while j >=0:
                    toRet.append(matrixCopy[j][0])
                    del matrixCopy[j][0]
                    j -=1
                if not matrixCopy or not matrixCopy[0]:
                    break
            return toRet
        else:
            return None

s = Solution()
print s.spiralOrder([[7],[9],[6]])
