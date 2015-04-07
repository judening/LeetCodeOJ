class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if len(s)<=1:
            return 0
        self.allCuts = []
        self.dfs([],s)
        return self.allCuts

    def isPanlidrome(self,s):
        if len(s)==1:
            return True
        else:
            return s[:] == s[::-1]

    def dfs(self,con,s):
        if not s:
            self.allCuts.append(con[:])
        else:
            for i in xrange(1,len(s)+1):
                if self.isPanlidrome(s[:i]):
                    con.append(s[:i])
                    print con
                    print s[:i]
                    self.dfs(con,s[i:])
                    con.pop()

S = Solution()
print S.minCut("aab")
