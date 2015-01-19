class Solution:
    def twoSum(self,num,target):
        dic = {}
        for i in xrange(len(num)):
            # I don't know why i need to point it out explicitly
            if dic.get(num[i]) is not None:
                print 'yes'
                return (i+1,dic[num[i]]+1)
            else:
                dic[target-num[i]] = i

S = Solution()
print S.twoSum([0,4,3,0],0)
