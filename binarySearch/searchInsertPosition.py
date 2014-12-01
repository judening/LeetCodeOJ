class Solution:
    def binarySearch(self,l,value):
        low = 0
        high = len(l)-1
        while low <= high:
            mid = (low+high)/2
            if l[mid] > value: high = mid - 1
            elif l[mid] < value: low = mid +1
            else: return mid
        return low

    def searchInsert(self,A,target):
        return self.binarySearch(A,target)
