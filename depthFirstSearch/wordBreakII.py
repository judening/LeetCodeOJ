class Solution:
    def wordBreak(self,s,dict):
        self.toRet = []
        cand = ''
        num = len(s)
        self.helper(cand,s,dict,num)
        return self.toRet

    def helper(self,cand,s,dict,num):
        if not s:
            return None
        else:
            for i in xrange(1,len(s)+1):
                if s[:i] in dict:
                    temp = self.helper(cand,s[i:],dict,num)
                    if not temp:
                        cand = s[:i]
                    else:
                        cand = s[:i] +' '+temp
                    tempString = cand.replace(' ','')
                    if num == len(tempString):
                        self.toRet.append(cand)
            return cand

s = Solution()
print s.wordBreak("ab",["a","b"])
print s.wordBreak('a',['a'])
print s.wordBreak('catsanddog',["cats","cat","and","sand","dog"])
