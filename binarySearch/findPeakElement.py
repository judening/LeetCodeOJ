class Solution:

    def findPeakElement(self,num):
        self.maxNumIndex = None
        self.binarySearch(num,None,0,len(num)-1)
        return self.maxNum

    def binarySearch(self,num,value,start,end):
        if start>end:
            return
        else:
            #avoid overflow
            mid = start + (end-start)/2
            if value:
                if num[mid] > value:
                    self.maxNum = mid
                    value = num[mid]
                else:
                    self.maxNum = mid
                    value = num[mid]
                self.binarySearch(num,value,start,mid-1)
                self.binarySearch(num,value,mid+1,end)
