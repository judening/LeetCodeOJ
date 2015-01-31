class Solution:
    def subsets(self,S):
        self.toRet = []
        S.sort()
        self.dfs([].S)
        self.toRet.append([])
        return self.toRet
    def dfs(self,cand,res):
        for i, e in enumerate(res):
            cand.append(e)
            temp = list(cand)
            self.toRet.append(temp)
            self.dfs(cand,res[i+1:])
            cand.pop()
