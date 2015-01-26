class Solution:
    def searchRange(self,A,target):
        if target < A[0] or target> A[-1]:
            return [-1,-1]
        else:
            self.ret = None
            self.mini = None
            self.maxi = None
            self.binarySearch(0,len(A)-1,A,target,-1)
            if self.mini is not None and self.maxi is not None:
                print 1
                self.ret = [self.mini,self.maxi]
            elif self.mini is not None and self.maxi is None:
                self.ret = [self.mini,self.mini]
            elif self.maxi and not self.mini:
                self.ret = [self.maxi,self.maxi]
            else:
                self.ret = [-1,-1]
            return self.ret
    def binarySearch(self,low,high,array,target,lastId):
        if low>high:
            if self.mini is not None:
                if lastId<self.mini and lastId !=-1:
                    self.mini = lastId
            if self.maxi is not None:
                if lastId>self.maxi:
                    self.maxi = lastId
            if self.mini is None and lastId != -1:
                self.mini = lastId
            if self.maxi is None and lastId != -1:
                self.maxi = lastId
        else:
            mid = (low+high)/2
            if array[mid] == target:
                self.binarySearch(low,mid-1,array,target,mid)
                self.binarySearch(mid+1,high,array,target,mid)
            else:
                self.binarySearch(low,mid-1,array,target,lastId)
                self.binarySearch(mid+1,high,array,target,lastId)

S = Solution()
print S.searchRange([1],1)
