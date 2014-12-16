class Solution:
    #This is the slower version of calculating the max area between two heights
    #Time complexity is O(n^2) and space complexity is O(n)
    def maxArea(self,height):
        if not height or len(height) == 1:
            return 0
        else:
            result = 0
            #To keep a most recent "highest height" array, we skip all the low heights (think about it if we keep them,
            #there will be duplicates if we calculate them) such that we save "some" time
            heightIndex = []
            heightIndex.append(0)
            #Iterating thru all the heights, calculating the max area up till the current height
            for i in xrange(1,len(height)):
                for j in xrange(len(heightIndex)):
                    ht = None
                    if height[i] > height[heightIndex[j]]:
                        ht = height[heightIndex[j]]
                    else:
                        ht = height[i]

                result = max((i-heightIndex[j])*ht,result)
                #if the index is higher than the last highest index, it's worth marking it down
                if height[i] > height[heightIndex[-1]]:
                    heightIndex.append(i)

            return result
