class Solution:

    def merge(self,A,m,B,n):
        j = 0
        i = 0
        d = 0
        #The whole m+d thing is to expand the size of A
        while i!=m+d and j!=n:
            if A[i] > B[j]:
                A.insert(i,B[j])
                j+=1
                d+=1
            i+=1
        while j!=n :
            A.insert(i,B[j])
            i+=1
            j+=1
        return A
