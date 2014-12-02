class Solution:

    def climbStairs(self,n):
        steps = [0,1,2]
        #The key intuition to solve the problem is that given a number
        #of stairs n, if we know the number ways to get to the points
        #[n-1] and [n-2] respectively, denoted as n1 and n2, then the
        #total ways to get to the point [n] is n1+n2. From the [n-1]point,
        #we can take one single step to reach [n] and form the [n-2]point,
        #we can take two steps to get there. There is NO overlapping
        #between the two solution sets, because we differ in the final
        #step
        for i in range(3,n+1):
            steps.append(steps[i-1]+steps[i-2])
        return steps[n]
