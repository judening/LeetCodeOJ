class Solution:
    def countAndSay(self,n):
        toRet = ["1"]
        i = 0
        while i < n-1:
            num = toRet[i]
            prep = num[0]
            k = 0
            temp =""
            for j in xrange(len(num)):
                if num[j] != prep:
                    temp = temp + str(k) + prep
                    k = 0
                    prep = num[j]
                k+=1
            temp = temp + str(k) + prep
            toRet.append(temp)
            i +=1
        return toRet[-1]
