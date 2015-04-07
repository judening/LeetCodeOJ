class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if len(num) ==1:
            return str(num[0])
        maxNum = max(num)
        maxLen = len(str(maxNum))
        dic = {}
        temp = list(num)
        for i in xrange(len(temp)):
            diff = maxLen - len(str(temp[i]))
            dic[str(temp[i])+diff*'0'] = i
            if diff>0:
                temp[i] = temp[i]*(10*diff)
        temp.sort()
        print dic
        print temp
        temp [:] = temp[::-1]
        ret = ''
        for i in temp:
            ret = ret+str(num[dic[i]])
        return ret

S = Solution()
print S.largestNumber([1,2])
