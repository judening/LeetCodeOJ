class Solution:
    def wordBreak(self,s,dict):
        self.toRet = []
        self.dfs(s,dict,'')
        return self.toRet

    #This problem can be broken down into 2 parts
    # 1.DP part
    # 2.DFS part

    # For the dp part, why is it dp?
    # Because
    def dpCheck(self,s,dict):
        dp = [False for i in xrange(len(s)+1)]
        dp[0] = True
        for i in xrange(1,len(s)+1):
            for k in range(0,i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]

    def dfs(self,s,dict,stringList):
        if self.dpCheck(s,dict):
            if not s:
                self.toRet.append(stringList[1:])
            for i in xrange(1,len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:],dict,stringList+' '+s[:i])

#    def helper(self,s,dict,currentIndex,fixLen):
#        if not s:
#            return None
#        else:
#            for i in xrange(1,len(s)+1):
#                if s[:i] in dict:
#                    self.helper(s[i:],dict,currentIndex+i,fixLen)
#                    for j in xrange(currentIndex+i,fixLen):
#                        tempArray = self.dp.get(j)
#                        if tempArray:
#                            print tempArray
#                            newList = list(tempArray)
#                            tempString = ''.join(newList)
#                            if currentIndex+i+len(tempString) == fixLen:
#                                newList.insert(0,s[:i])
#                                print newList
#                                self.dp[i-1] = newList
#                            if len(tempString)+len(s[:i]) == fixLen:
#                                self.toRet.append(' '.join(newList))
#                    else:
#                        if currentIndex+i == fixLen:
#                            tempArray = self.dp[currentIndex+i-1]
#                            if not tempArray:
#                                self.dp[currentIndex+i-1].append(s[:i])
#            return
#
s = Solution()
print s.wordBreak('a',['a'])
print s.wordBreak('catsanddog',["cats","cat","and","sand","dog"])
