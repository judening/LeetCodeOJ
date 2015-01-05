class Solution:

    def wordBreak(self,s,dict):
        self.dic = {"":True}
        return self.helper(s,dict)

    def helper(self,s,dict):
        if s in self.dic:
            return self.dic[s]
        for i in xrange(1,len(s)+1):
            if s[:i] in dict and self.helper(s[i:],dict):
                self.dic[s] = True
                return True
        self.dic[s] = False
        return False
