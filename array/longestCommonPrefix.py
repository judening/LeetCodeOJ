class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        minimumIndex = 0
        maxString = ""
        if len(strs)>1:
            minimumIndex = len(strs[0])
            lastChar = strs[0]
            maxString = strs[0]
            for i in xrange(1,len(strs)):
                minimumIndex = min(len(strs[i]),minimumIndex)
                for a in xrange(minimumIndex):
                    if strs[i][a] != lastChar[a]:
                        if minimumIndex == 1:
                            return ""
                        else:
                            minimumIndex = a
                if len(strs[i])>len(maxString):
                    maxString = strs[i]
                lastChar = strs[i]
            return maxString[:minimumIndex]
        elif len(strs) == 1:
            return strs[0]
        else:
            return ""

S = Solution()
print S.longestCommonPrefix(["flower","flo","flight"])

