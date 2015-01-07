class Solution:
    # This problem is really hard to understand
    def singleNumber(self, A):
        ones = 0
        twos = 0
        threes = 0
        # There are a lot going on here
        # Let's say if a number appear three times
        # The first time, it sets ones to that number
        for num in A:
            # First time, twos = 0.
            # Second time, twos = num since ones = num
            # Third time, (ones&num) = 0 but twos already = num, so twos = num
            twos = twos| (ones&num)
            # First time, ones = num
            # Second time, ones = 0 since "^" 1^1=0
            # Third time, ones = num again
            ones = ones ^ num
            # Both zeros for the first and second time because either ones=0 or twos = 0
            # Third time threes = num since ones= num and twos = num
            threes = one&twos
            # Here, for the first times, it will not affect ones since ~threes = 1
            # Same for the second time! whatever ones is, ~threes will not affect it
            # For the third time, it will reset ones back to zero since ~threes is the opposite of num
            ones = ones& ~threes
            # Same for twos
            twos = twos& ~threes

        return ones
