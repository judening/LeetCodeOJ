class Solution:
    def countAndSay(self,n):
        counter = 1
        last = "1"
        nth = int(n)
        while counter < nth:
            subCounter = 0
            subLast = last[0]
            temp = ""
            for char in last:
                if subLast is not char:
                    temp = temp + str(subCounter) + subLast
                    subCounter = 1
                    subLast = char
                else:
                    subCounter = subCounter + 1

            temp = temp + str(subCounter) + subLast
            last = temp
            counter = counter + 1
        return last
