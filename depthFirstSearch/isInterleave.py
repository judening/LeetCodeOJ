class Solution:

    def isInterleave(self,s1,s2,s3):
        if len(s1)+len(s2) != len(s3):
            return False
        else:
            return self.helper(s1,s2,s3)

    def helper(self,s1,s2,s3):
        if s1 and s2:
            if s1[0] == s3[0] and s2[0] == s3[0]:
                return self.helper(s1[1:],s2,s3[1:]) or self.helper(s1,s2[1:],s3[1:])
            elif s1[0] == s3[0]:
                return self.helper(s1[1:],s2,s3[1:])
            elif s2[0] == s3[0]:
                return self.helper(s1,s2[1:],s3[1:])
            else:
                return False
        elif s1 and not s2:
            if s1[0] == s3[0]:
                return self.helper(s1[1:],s2,s3[1:])
            else:
                return False
        elif s2 and not s1:
            if s2[0] == s3[0]:
                return self.helper(s1,s2[1:],s3[1:])
            else:
                return False
        else:
            return True

S = Solution()
print S.isInterleave('aabcc','dbbca','aadbbcbcac')
print S.isInterleave('aabcc','dbbca','aadbbbaccc')
