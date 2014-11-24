#Some intersting questions to think about before coding
# 1. Reversed integer overflow? 214748364
# 2. What's the outpul for integer like 10,100?
# 3. The original integer overflow?

class Solution:
    def reverse(self,x):
        ret = 0
        flag = False
        if x < 0:
            flag = True
            x = abs(x)
        while x !=0:
            if x > 2147483647
                return 0
            ret = ret * 10 + x%10
            x = x/10
        if ret > 2147483647:
            return 0
        if flag:
            ret = ret*-1
        return ret
