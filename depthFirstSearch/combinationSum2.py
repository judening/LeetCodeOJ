class Solution:
    def combinationSum2(self,candidates,target):
        res = []
        cand = []
        candidates.sort()
        self.dfs(candidates,cand,target,res)
        return res

    def dfs(self,candidates,cand,target,res,prev = None):
        if target < 0:
            return
        elif target == 0:
            res.append(cand[:])
        else:
            for i, c in enumerate(candidates):
                # Every single time, we use THIS to eliminate the changes
                if i == 0:
                    prev = c
                # The prev is used inside This for loop, it has Nothing
                # to do with the dfs function
                elif prev == c:
                    continue
                cand.append(c)
                self.dfs(candidates[i+1:],cand,target-c,res,prev)
                cand.pop()
