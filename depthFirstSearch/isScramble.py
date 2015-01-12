class Solution:
    # one hit true, then true
    def isScramble(self,s1,s2):
        if not s1 or not s2 or len(s1)!=len(s2):
            return False
        if s1 == s2:
            return True
        temp1 == ''.join(sorted(s1))
        temp2 == ''.join(sorted(s2))
        if temp1 != temp2:
            return False
        for i in xrange(len(s1)):
            # OK, I understand this, but what about the next condition?
            if self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            # Ok, this is a bit odd. see example great/eatgr
            if self.isScramble(s1[0:i],s2[len(s2)-i:]) and self.isScramble(s1[i:],s2[0:len(s2)-i]):
                return True
        return False

