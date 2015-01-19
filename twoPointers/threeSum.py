class Solution:
    def threeSumClosest(self,num,target):
        combSet = []
        comb = []
        size = len(num)

        if size<3:
            return None
        else:
            # The reason to sort them is only to traverse them forward
            # and not going backward
            # Also, if we sort them, we know that the list is ascending
            num.sort()
            lastGap = None
            toRet = None
            # why len(num)-2? because we will never hit num[len(num)-2]
            # for i because of three sum
            for i in range(len(num)-2):
                start = i +1
                end = len(num)-1

                # The reason of this while loop is we keep incrementing the start and decrementing the end
                while start < end:
                    threeSum = sum([num[i],num[start],num[end]])
                    gap = threeSum - target
                    # Obviously, if gap is zero, we cannot get better
                    if gap == 0:
                        return threeSum

                    if lastGap:
                        if abs)gap) < lastGap:
                            lastGap = abs(gap)
                            toRet = threeSum
                    else:
                        lastGap = abs(gap)
                        toRet = threeSum

                    # There is only one choice
                    # Since the array is ascending, the end of the array is always greater than the start of the array
                    # If we get a larger gap, we can choose to minus the end
                    if gap>0:
                        end = end - 1
                    # If we get a smaller gap, we can choose to plus the start
                    if gap<0:
                        start = start +1
            return toRet

