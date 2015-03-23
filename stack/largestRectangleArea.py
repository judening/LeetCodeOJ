class Solution:
    # Essentially, this is a bucket effect
    def largestRectangleArea(self,height):
        if not height:
            return 0
        if len(height) == 1:
            return height[0]
        stack = []
        max_area = 0
        n = len(height)
        for i in range (n+1):
            # You hit the shorter board (shorter than the last one)
            # And you hit the last board
            while stack and (i == n or height[stack[-1]] > height[i]):
                h = height[stack.pop()]
                if stack :
                    w = i - stack[-1]-1
                else:
                    # Last one in the stack
                    w = i
                max_area = max(max_area, h*w)
            # Record the index position, for 1. deciding the width what calculating the area
            # 2. deciding if we hit the next short
            stack.append(i)
        return max_area


