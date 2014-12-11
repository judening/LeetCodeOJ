class Solution:

    def removeDuplicates(self,A):
        if not A:
            return 0
        else:
            i = 1
            j = 1
            while i < len(A):
                #This is a little bit not intuitive
                #So the logic here is when A[prev/i] == A[counter/j]
                #We keep moving counter
                #And we only need to return i, and they're all unique
                #different numbers
                i = 1
                j = 1
                while i < len(A):
                    if A[j-1] != A[i]:
                        A[j] = A[i]
                        j +=1
                    i+=1
                return j
