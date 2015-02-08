class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.toRet = []
        cand = []
        temp = ''
        self.dfs(s,[],0,temp)
        return self.toRet

    def dfs(self,s,cand,counter,temp):
        if not s and counter==4:
            print cand
            self.toRet.append(".".join(cand[:]))
        else:
            if counter<4:
                for i in xrange(len(s)):
                    if not temp:
                        temp = s[i]
                        if int(temp)<=255 and int(temp)>=0:
                            cand.append(temp)
                            self.dfs(s[1:],cand,counter+1,temp)
                    else:
                        temp +=s[i]
                        if len(temp)<=3 and int(temp)<=255 and int(temp)>=0:
                            cand.append(temp)
                            self.dfs(s[1:],cand,counter+1,temp)
                        else:
                            cand.append(s[i])
                            self.dfs(s[1:],cand,counter+1,s[i])

S = Solution()
print S.restoreIpAddresses("0000")
