class Solution:

    def longestPalindrome(self,s):
        left = 0
        longest = 0
        dp = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        for i in xrange(len(s)):
            for j in xrange(i+1):
                # When we are far away from center,
                # we need to know the narrower string's true/false, which
                # is recorded in the last run of for loop
                if i-j>=2:
                    if s[i] == s[j] and dp[j+1][i-1]:
                        dp[j][i] = True
                    else:
                        # We hit the center, and only one char is the center
                        if i==j:
                            dp[j][i] = True
                        # We hit the center, and two chars are the center
                        else:
                            if s[i] == s[j]:
                                dp[j][i] = True
                # Update longest for each run
                if(i-j+1>=longest and dp[j][i]):
                    longest = i-j+1
                    left = j
                    right = i
        return s[left:right+1]
