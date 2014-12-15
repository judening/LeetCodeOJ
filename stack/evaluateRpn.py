class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        operations = ['+','-','*','/']
        if len(tokens) < 2:
            return int(tokens[0])
        else:
            for i in tokens:
                if i not in operations:
                    stack.append(i)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if i == '+':
                        stack.append(int(b) + int(a))
                    elif i == '-':
                        stack.append(int(b) - int(a))
                    elif i == '*':
                        stack.append(int(b) * int(a))
                    else:
                        stack.append(int(float(int(b)) / int(a)))
            return stack.pop(0)
