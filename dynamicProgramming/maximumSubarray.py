class Solution:

    def maxSubArray(self,A):
        B = []
        pre = None
        for i in A:
            if not pre:
                pre = i
                B.append(pre)
            else:
                pre = max(i,pre+i)
                B.append(pre)
        return max(B)
