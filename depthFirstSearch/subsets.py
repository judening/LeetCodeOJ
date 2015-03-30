class Solution:
    def subsets(self,S):
        self.toRet = []
        S.sort()
        self.dfs([].S)
        self.toRet.append([])
        return self.toRet
    def dfs(self,cand,res):
        # One of the mistakes that can be easily made is that
        # we add the cand only when res is empty
        # Yet, since we are doing a DFS and we keep popping, so it's really easily
        # missing some of the values
        for i, e in enumerate(res):
            cand.append(e)
            # One thing to note that is here
            # We create a deep copy of the list
            # Then we add the list to the final return
            temp = list(cand)
            self.toRet.append(temp)
            self.dfs(cand,res[i+1:])
            cand.pop()
