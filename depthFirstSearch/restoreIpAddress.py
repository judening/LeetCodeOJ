import re
class Solution:
    # @param s, a string
    # @return a list of strings
    # 11:04
    def restoreIpAddresses(self, s):
        output, temp = [], []
        self.findSection(s, output, temp)

        return output

    def findSection(self, s, output, temp):
        if len(temp) == 4:
            if s:
                return
            else:
                output.append('.'.join(temp))
                return

        for i in range(1, 4):
            # re.findall('^0\d+',s[:i]) means that if 0 is more than 2
            # It is out of the question
            if i > len(s) or re.findall('^0\d+', s[:i]) or int(s[:i]) > 255:
                return
            temp.append(s[:i])
            self.findSection(s[i:], output, temp)
            temp.pop()



S = Solution()
print S.restoreIpAddresses("0000")
