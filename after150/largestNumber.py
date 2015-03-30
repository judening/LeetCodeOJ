class Solution:

    def largestNumber(self,num):
        maxLen = 0
        for char in num:
            if len(str(char)) > maxLen:
                maxLne = len(str(char))
        dic = {}
        temp = list(num)
        for i in xrange(len(temp)):
            diff = maxLen - len(str(temp[i]))
            dic[str(temp[i])]
