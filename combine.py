class Solution:

    def combine(self,n,k):
        if k>n:
            return []
        else:
            myList = list(xrange(1,n+1))
            return self.permute(myList,k)

    def permute(self,num,k):
        if len(num) == 1:
            return [num]
        if len(num) == 0:
            return []

        toRet = []


        for index in range(len(num)):
            subNum = num[index+1:]
            z = self.permute(subNum,k)
            for t in z:
                if len(t)<k+1:
                    toRet.append([num[index]]+t)
                else:
                    if not t in toRet:
                        toRet.append(t)

        return toRet

a = Solution()
c = a.combine(2,1)
print c
