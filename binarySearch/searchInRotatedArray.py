class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        def s(A,target,start,end):
            if start > end:
                return -1
            mid = (start+end)/2
            if A[mid] == target:
                return mid
            # You can be sure that (A[start] and A[mid] are in the same half)
            if A[start] <= A[mid]:
                # This condition ensure that target is in the (start,mid) half
                if A[start] <= target and target<A[mid]:
                    return s(A,target,start,mid-1)
                else:
                    return s(A,target,mid+1,end)
            # You can be sure that (A[mid] and A[end] are in the same half)
            if A[start] > A[mid]:
                # This condition ensure that target is in the (mid,end) half
                if A[mid] <target and target <=A[end]:
                    return s(A,target,mid+1,end)
                else:
                    return s(A,target,start,mid-1)
        return s(A,target,0,len(A)-1)
