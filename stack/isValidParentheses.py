class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in s:
            if i == ')':
                try:
                    j = stack.pop()
                    if j != '(':
                        return False
                except IndexError:
                    return False
            elif i == ']':
                try:
                    j = stack.pop()
                    if j != '[':
                        return False
                except IndexError:
                    return False
            elif i == '}':
                try:
                    j = stack.pop()
                    if j != '{':
                        return False
                except IndexError:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
