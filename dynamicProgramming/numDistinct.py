class Solution:
    # Given two sequences S,T, how many unique ways in sequence S, to form
    # a subsequence that is identical to the sequence T.
    # e.g.
    # S= "rabbbit", T= "rabbit"
    # The number is 3. And the formations as follows:
    # S1 = "ra_bbit" S2 = "rab_bit" S3="rabb_it"
    # "_" marks the removed character
    def numDistinct(self,S,T):
        # As a typical way to implement a DP algorithm, we construct a matrix dp,
        # where each cell dp[i][j] represents the number of solutions of aligning
        # substring T[0..i] with S[0..j]
        sl = len(S)
        tl = len(T)

        # Rule 1. dp[0][j] = 1, since aligning T = "" with any substring of S
        # would have only ONE solution,which is to delete all characters in S.
        dp = [[None for i in xrange(sl+1)] for j in xrange(tl+1)]

        # On the other hand, aligning T="rabbit" with S = "" would just be zero!
        for i in xrange(sl+1):
            dp[0][i] = 1
        for j in xrange(1,tl+1):
            dp[j][0] = 0
        for t in xrange(1,tl+1):
            for s in xrange(1,sl+1):
                # Rule 2. when i>0, dp[i][j] can be derived by two cases:
                # 1). if T[i] != S[j], then the solution would be ignore the character
                #     s[j] and align substring T[0..i] with S[0..j-1].Therefore,
                #     dp[i][j] = dp[i][j-1]
                if T[t-1] != S[s-1]:
                    dp[t][s] = dp[t][s-1]
                # 2). if T[i] == S[j], then first we could adpot the solution in case 1,
                #     but also we could match the characters T[i] and S[j] and align the
                #     rest of them (i.e. T[0..i-1] and S[0..j-1]) As a result,
                #     do[i][j] = dp[i][j-1] + d[i-1][j-1]
                else:
                    dp[t][s] = dp[t][s-1] + dp[t-1][s-1]
        return dp[tl][sl]

S = Solution()
print S.numDistinct("rabbbit","rabbit")


