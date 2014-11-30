class Solution:

    def reverse(self,x):
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        #Memorize this for reversing anything
        ret = str(x)[::-1]
        numRet = int(ret)
        if numRet>2147483647
            return 0
        if flag:
            numRet = numRet*-1
        return numRet
