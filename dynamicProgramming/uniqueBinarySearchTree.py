class Solution:

    #For catalan numbers, the recurrence relationship is shown below
    def numTrees(self,n):
        totalTrees = []
        totalTrees.extend([1,1])
        for j in range (2,n+1):
            recurrenceSum = 0
            for i in range(j):
                recurrenceSum = recurrenceSum + totalTrees[i]*totalTrees[j-i-1]
            totalTrees.append(recurrenceSum)
        return totalTrees[-1]
