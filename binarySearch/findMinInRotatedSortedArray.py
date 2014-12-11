class Solution:
    def findMin(self,num):
        start = 0
        end = len(num)-1

        if len(num) == 1:
            return num[0]

        while num[start] > num[end]:
            mid = start + (end-start)/2

            if num[start]>num[mid]:
                end = mid

            elif num[start] < num[mid]:
                start = mid
            else:
                return num[end]
        return num[start]
