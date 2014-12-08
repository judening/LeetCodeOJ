class Soltuion:
    def maxProduct(self,A):
        minTemp = A[0]
        maxTemp = A[0]
        maxVal = A[0]
        #It is smart to keep the min/max temp under 2 variables.
        #The thing is, regardless of current A[i] greater/lesser 0, setting two temp variables and making
        #them always = the smallest/greatest product of possible combination helps maintain the most current
        #maxVal of consecutive array
        for i in range(1,len(A)):
            minTemp, maxTemp = min(A[i],A[i]*maxTemp,A[i]*minTemp),max(A[i],A[i]*minTemp,A[i]*maxTemp)
            maxVal = max(maxVal,maxTemp)
        return maxVal

