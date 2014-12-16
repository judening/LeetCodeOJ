class Solution:
    # Proved by contradiction:
    # Suppose the resurned result is not the optimal solution. Then there must exist an
    # optimal solution, say a container with an optimal left(aol) and an optimal right(aor
    # ),such that it has a greater volume than the one we got. Since our algorithm stops
    # only if the two pointers meet. So, we must have visited one of them but not the other
    # . WLOG, let's say we visited aol but not aor. When a pointer stops at aol,it won't
    # move until
    #    * The other pointer also points to aol. In this case, iteration ends. But the
    #      other pointer must have visited aor on its way from right end to aol. Contradiction
    #      to our assumption that we didn't visit aor.
    #
    #    * The other pointer arraives at a value,say arr, that is greater than aol before it reaches
    #      aor. In this case, we do move aol. But notice that the volume of aol and arr is already
    #      greater than aol and aor (as it is wider and heigher), which means that aol and aor is
    #      not the optimal solution -- Contradiction!
    def maxArea(self,height):
        left = 0
        right = len(height)-1
        result = 0

        while left<right:
            #area is decided by the shorter wood board
            result = max(result,(right-left)*min(height[left],height[right]))
            #we will keep the short limit untill the max area of "this short limit" is
            #calculated
            if height[left] < height[high]:
                left +=1
            else:
                right -=1

        return result
