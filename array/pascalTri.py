class Solution:

    def generate(self,numRows):
        basic = [0,1,0]
        toRet = []
        if numRows >= 1:
            toRet.append([1])
            lastList = basic
            for i in xrange(numRows-1):
                newList = []
                for j in xrange(1,len(lastList)):
                    newList.append(lastList[j-1]+lastList[j])
                toRet.append(list(newList))
                newList.insert(0,0)
                newList.append(0)
                lastList = newList
        return toRet
