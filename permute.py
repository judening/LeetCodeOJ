class Solution:

    def permute(self,num):
        if len(num) == 1: return [num]
        if len(num) == 0: return []

        toRet = []

        for index in range(len(num)):
            subNum = num[0:index] + num[index+1:]
            z = self.permute(subNum)
            for t in z:
                toRet.append([num[index]]+t)
        return toRet


a = Solution()
b = a.permute([1,2,3])
print b
