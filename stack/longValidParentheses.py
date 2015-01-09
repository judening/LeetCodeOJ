class Solution:

    def longestValidParentheses(self,s):
        stack = []
        maxLen = 0
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    lastPos = -1
                    # it will keep incrementing the length of valid parentheses
                    if stack:
                        lastPos = stack[-1]

                    curLen = i - lastPos
                    maxLen = max(maxLen,curLen)
                else:
                    stack.append(i)
        return maxLen
