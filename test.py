class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        lastSpace = None
        for i in reversed(xrange(len(s))):
            if s[i] == ' ':
                lastSpace = i
                break
        if lastSpace:
            s[:] = s[-lastSpace:] + s[:-lastSpace]


S = Solution()
s = ["a"," ","b"]
S.reverseWords(s)
print s









