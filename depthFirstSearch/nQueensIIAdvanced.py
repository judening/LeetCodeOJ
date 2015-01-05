class Solution:
    def totalNQuees(self,n):
        self.res = []
        state = [-1 for i in xrange(n)]
        self.helper(state,0)
        num = len(self.res)
        return num

    def helper(self,state,row):
        n = len(state)
        if row == len(state):
            arry = [["." for i in xrange(n)] for j in xrange(n)]
            for i in xrange(n):
                arry[i][state[i]] = 'Q'
            self.res.append(arry)
            return
        for i in xrange(len(state)):
            if self.isValid(state,row,i):
                state[row] = i
                self.helper(state,row+1)
                state[row] = -1

    def isValid(self,state,row,col):
        for i in xrange(row):
            # The first condition check if different rows will have the same 'Q'
            # The second condition is REALLY SUBTLE!! Think as (row-i)/(col-state[i]) = +-1
            # This is exactly checking if the slope is 45 degree
            if state[i] == col or abs(row-i) == abs(col-state[i]):
                return False
        return True
