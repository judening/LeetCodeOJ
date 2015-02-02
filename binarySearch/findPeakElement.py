class Solution:
    # Remember it needs O(logn)
    # If you don't do a if conditions, you will endup finding the array
    # O(n)
    def findPeakElement(self, num):
        if num:
            l = 0
            r = len(num)-1
            while (l < r):
                mid = (l+r)/2
                if num[mid] > num[mid-1] and num[mid] > num[mid+1]:
                    return mid
                elif num[mid] < num[mid-1]:
                    r = mid
                else:
                    l = mid+1
            if num[0] > num[len(num)-1]:
                return 0
            else:
                return len(num)-1
        else:
            return 0
