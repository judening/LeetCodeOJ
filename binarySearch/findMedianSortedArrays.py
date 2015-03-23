#Using divide and conquer idea, each time find the mid of both arrays
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        # A
        m = len(A)
        n = len(B)

        k = (m+n+1)/2
        #The goal is find the kth element
        v = float(self.findKth(A,0,m-1,B,0,n-1,k))

        if (m+n)%2 == 0:
            k2 = k+1
            v2 = self.findKth(A,0,m-1,B,0,n-1,k2)
            v = (v+v2)/2

        return v

    # find the kth element in the two sorted arrays
    # let us say: A[aMid] <= B[bMid], x: min len of a, y:mid len of b
    # Then, we can know the followings:
    # (1). there will be at least (x+y+1) elements before bMid
    # (2). there will be at least (m-x-1+n-y) = m+n- (x+y+1) elements after aMid
    # Therefore,
    # if k <= x+y+1, find the kth element in a and b, but unconsidering bMid and
    # its suffix
    # if k > x+y+1 find the k-(x+1)th element in a and b without considering aMid
    # and its prefix
    def findKth(self,A,aL,aR,B,bL,bR,k):
        if (aL > aR):
            return B[bL+k-1]
        if (bL > bR):
            return A[aL+k-1]

        aMid = (aL+aR)/2
        bMid = (bL+bR)/2
        if (A[aMid] <= B[bMid]):
            if (k<= aMid-aL + bMid-bL+1):
                return self.findKth(A,aL,aR,B,bL,bMid-1,k)
            else:
                return self.findKth(A,aMid+1,aR,B,bL,bR,k-(aMid-aL)-1)
        else:
            if (k<= aMid-aL + bMid-bL+1):
                return self.findKth(A,aL,aMid-1,B,bL,bR,k)
            else:
                return self.findKth(A,aL,aR,B,bMid+1,bR,k-(bMid-bL)-1)
