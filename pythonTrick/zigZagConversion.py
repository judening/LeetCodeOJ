class Solution:
    # @return a string
    # This is using slice trick and the try expect trick
    def convert(self, s, nRows):
        res = [[] for _ in range(nRows)]
        i = 0
        try:
            while True:
                for r in res:
                    r.append(s[i])
                    i += 1
                # This is very smart. when you hit the bottom of the list
                # you go back to the top starting to the second to the last
                # one, which in this case is A[-2] and end at 1
                for r in res[-2:0:-1]:
                    r.append(s[i])
                    i += 1
        except IndexError:
            return ''.join(''.join(r) for r in res)
