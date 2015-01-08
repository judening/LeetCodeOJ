class Solution:
    def atoi(self,str):
        # First trick here!! To use strip func
        str = str.strip()
        if len(str) == 0:
            return 0
        if str[0] in '+-':
            s = str[0]
            i = 1
        for i in xrange(i,len(str)):
            # Second trick!
            # I didn't know i can actually check if a string is within
            # a range like within (0,9), or within (a,z), or within (A,Z)
            if '0' <= str[i] <= '9':
                r = r*10 + int(str[i])
            else:
                break
            if s == '-':
                r *=-1
            if r > 214748367:
                r = 214748367
            if r < -214748368
                r = -214748368
            return r
