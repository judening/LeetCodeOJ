class Solution:
    def findMin(self,num):
        return self.binarySearch(0,len(num)-1,num)
    def binarySearch(self,low,high,num):
        if low>= high:
            return num[low]
        else:
            mid = (low+high)/2
            # It is rotated,mid at first half, minimum must be in the second half
            if num[mid] > num[low] and num[mid]>num[high]:
                return self.binarySearch(mid+1,high,num)
            # normal order, keep looking it in the first half
            if num[mid] > num[low] and num[mid]<=num[high]:
                return self.binarySearch(low,mid-1,num)
            # mid at second half, but not sure if mid is the minimum, so keep incrementing
            # low
            if num[mid] <= num[low] and num[high]<num[low]:
                return self.binarySearch(low+1,high,num)
            # Duplicates keep happening!!!!
            if num[mid] <= num[low] and num[high]>=num[low]:
                if high-low == 1:
                    return num[low]
                else:
                    return self.binarySearch(low+1,high-1,num)
