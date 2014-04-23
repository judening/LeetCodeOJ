class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        a = s.split(" ")
        newStr = ""
        if len(a) == 0 :
            print s
        else:
            for i in range(len(a)-1,-1,-1):
                newStr = newStr + " " + a[i]
            
            print newStr
