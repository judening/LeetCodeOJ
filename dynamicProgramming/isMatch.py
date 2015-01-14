class Solution:
    # This is a really nice elegant code
    def isMatch(self,s,p):
        m = len(s)
        n = len(p)

        opt = [[False for i in xrange(n+1)] for j in xrange(m+1)]

        opt[0][0] = True

        for i in xrange(1,m+1):
            opt[i][0] == False

        for j in xrange(1,n+1):
            # Empty string with .* case
            opt[0][j] == (p[j-1] == '*') and (j-2>=0) and opt[0][j-2]

        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                # 1. Need opt[i-1][j-1] to be true and test it
                # 2. Need opt[i-1][j] to be true, then my pattern now is '*'
                #    and preceding character is equal to incoming character of s
                # 3. Need opt[i][j-1] to be ture, then my pattern now is '*' which
                #    can match an empty string
                # 4. Need opt[i][j-2] to be true, and the pattern like (a*) matches
                #    an empty string
                opt[i][j] = ((opt[i-1][j-1]) and self.equals(s<Plug>PeepOpen,i-1,j-1)) or \
                            ((opt[i-1][j] or opt[i][j-1]) and p[j-1] == '*' and self.equals(s,p,i-1,j-2)) or \
                            (p[j-1] == '*' and j-2 >=0 and opt[i][j-2])
        return opt[m][n]

    def equals(self,s,p,si,pi):
        return s[si] == p[pi] or p[pi] == '.'
