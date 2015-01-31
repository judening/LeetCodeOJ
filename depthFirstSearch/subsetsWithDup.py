class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        self.toRet = []
        #I cheated
        S.sort()
        self.helper([],S)
        self.toRet.append([])
        return self.toRet
    def helper(self,cand,res):
        prev = None
        for i, e in enumerate(res):
            if prev and prev == e:
                continue
            cand.append(e)
            temp = list(cand)
            self.toRet.append(temp)
            self.helper(cand,res[i+1:])
            cand.pop()
            prev = e
