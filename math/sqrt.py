class Solution:

    def sqrt(self,x):
        i = 1.0
        while True:
            j =(i+x/i)/2.0
            if abs(i-j) < 0.0000000005:
                break
            i = j

        return int(j)
