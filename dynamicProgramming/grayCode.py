class Solution:
    #Gray code makes use of both dynamic programming and recusion
    def grayCode(self,n):
        if n == 0:
            toRet = []
            toRet.append(0)
            return toRet

        #get the last rez with n-1
        rez = self.grayCode(n-1)

        addNum = 1<<(n-1)
        #tadah, in python, you can't modify the list when you iterate them
        newRez = list(rez)

        #make use of the last rez and add one from end to start
        for i in range(len(rez)-1,-1,-1):
            newRez.append(addNum+rez[i])

        return newRez
