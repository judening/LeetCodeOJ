class Solution:
    # This will not pass the leetcode b/c python's dynamic typing system
    def longestPalindrome(self,s):
        length = len(s)
        while length>0:
            for i in xrange(len(s)-length+1):
                left = i
                right = i+length-1
                good = True

                while left<right:
                    if s[left] != s[right]:
                        good = False
                        break
                    left +=1
                    right -=1

                if good:
                    return s[i:i+length]
            length -=1
        return ''
