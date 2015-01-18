class Solution:
    def merge(self,A,m,B,n):
        i = 0
        j = 0
        while i<m and j<n:
            if A[i]>B[j]:
                A.insert(i,B[j])
                j+=1
            else:
                i+=1
        if B:
            A.extend(B[j:])
