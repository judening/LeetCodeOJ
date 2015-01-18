class Solution:
    def majorityElement(self,num):
        dic = {}
        maxTime = 0
        toRet = None
        for i in xrange(len(num)):
            if dic.get(num[i]):
                dic[num[i]] +=1
            else:
                dic[num[i]] = 1
        for key in dic.keys():
            if dic[key] > maxTime:
                maxTime = dic[key]
                toRet = key
        return toRet
