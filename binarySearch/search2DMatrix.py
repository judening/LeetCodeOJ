class Solution:
    # Do not treat the matrix as a 2d array, multiply m*n and treat it
    # as an array
    def searchMatrix(self,matrix,target):
        if matrix:
            return self.binarySearch(0,len(matrix)*len(matrix[0])-1,matrix,target)
        else:
            return False

    def binarySearch(self,low,high,matrix,target):
        if low>high:
            return False
        else:
            m = (low+high)/2
            row = m/len(matrix[0])
            col = m%len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]<target:
                return self.binarySearch(m+1,high,matrix,target)
            else:
                return self.binarySearch(low,m-1,matrix,target)

S = Solution()
print S.searchMatrix([[1]],0)
