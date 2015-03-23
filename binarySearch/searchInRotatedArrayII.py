class Solution:
    def search(self,A,target):
        def s(A,target,start,end):
            if start > end:
                return False
            mid = (start+end)/2
            if A[mid] == target:
                return True
            # Possible normal order
            if A[start] < A[mid]:
                # Target must be in the normal order part
                if A[start] <= target and target < A[mid]:
                    return s(A,target,start,mid-1)
                else:
                    return s(A,target,mid+1,end)
            # Must be rotated order
            if A[start] > A[mid]:
                # The range is in the lesser part
                if A[mid] < target and target <= A[end]:
                    return s(A,target,mid+1,end)
                # The range is in the greater part
                else:
                    return s(A,target,start,mid-1)
            # You literally just need to search for both parts
            if A[start] == A[mid]:
                return s(A,target,start,mid-1) or s(A, target,mid+1,end)
        return s(A,target,0,len(A)-1)

