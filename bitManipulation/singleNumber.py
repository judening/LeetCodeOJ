# This is probably one of the smartest methods I've ever seen
class Solution:
    def singleNumber(self,A):
        #The logic behind this is XOR
        #Say A XOR A = 0, and A XOR B XOR A = B
        #Now the code becomes ridiculously easy

        a = 0
        for num in A:
            a = a ^ num

        return a

solution = Solution()
testCase = [2,3,4,5,3,4,2]
print solution.singleNumber(testCase)
