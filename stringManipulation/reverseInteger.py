#Some intersting questions to think about before coding
# 1. Reversed integer overflow? 214748364
# 2. What's the outpul for integer like 10,100?
# 3. The original integer overflow?
# 4. Better to use build-in string reverse?

class Solution:
    def reverse(self,x):
        ret = 0
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        if x > 2147483647
            return 0
        ret = str(x)[::-1]
        numRet = int(ret)
        if numRet > 2147483647:
            return 0
        if flag:
            numRet = numRet*-1
        return numRet
