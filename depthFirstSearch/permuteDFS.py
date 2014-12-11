class Solution:
    def permute(self,num):
        self.toRet = []
        cand = []
        self.helper(cand,num)

        return self.toRet

    def helper(self,cand,res):
        if len(res) == 0
            self.toRet.append(cand[:])
        else:
            for i, e in enumerate(res):
                cand.append(e)
                self.helper(cand,res[:i]+res[i+1:])
                cand.pop()
