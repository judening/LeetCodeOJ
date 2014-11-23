#Given an array of integers, every element appears *twice* except for one
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        table = {}

        for i in A:
            if not table.get(i):
                table[i] = 1
            else:
                #This totally avoids iterating the keys again
                del table[i]
        keys = table.keys()
        return keys[0]
