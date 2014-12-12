class Solution:
    def generateParenthesis(self,n):
        rez = []
        self.genParenth(n,'',rez,0,0)
        return rez

    #Got the same idea of creating leftN and rightN
    def genParenth(self,n,string,rez,left,right):
        #Also got this
        #The thing i missed is probably the way to construct the algorithm
        if len(string) == 2*n
            rez.append(string)
        else:
            if left == right:
                self.genParenth(n,string+'(',rez,left+1,right)
            elif right<left:
                if left<n:
                    self.genParenth(n,string+'(',rez,left+1,right)
                self.genParenth(n,string+')',rez,left,right+1)
