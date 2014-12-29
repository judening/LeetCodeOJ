class Solution:
    def wordBreak(self,s,dict):
        if not s:
            return True
        for i in xrange(1,len(s)+1):
            if s[0:i] in dict and self.wordBreak(s[i:],dict):
                return True

        return False

dict = ['i','like','sam','sung','samesung','mobile','ice','cream',
        'icecream','man','go','mango']
s = Solution()
print s.wordBreak('i',dict)
print s.wordBreak('ilike',dict)
print s.wordBreak('iiiiiiiiiiii',dict)
print s.wordBreak('jkjkjk',dict)
print s.wordBreak('',dict)
print s.wordBreak('ilikesamesungmangoicecream',dict)


