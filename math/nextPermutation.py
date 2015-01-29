class Solution:
    def nextPermutation(self,num):
        if len(num)<=1:
            return num
        else:
            # Step 1. Find the first number that break the increasing trend
            # From "right to left"
            splitIndex = -1
            for i in xrange(len(num)-2,-1,-1):
                if num[i] < num[i+1]:
                    splitIndex = i
                    break
            # Step 2. Find the first number that is greater than
            # num[splitIndex] from "right to left"
            replaceIndex = len(num)-1
            while replaceIndex > splitIndex:
                if num[replaceIndex] > num[splitIndex}:
                    break
                replaceIndex -=1
            # Step 3. Swap the two values
            num[replaceIndex],num[splitIndex] = num[splitIndex],num[replaceIndex]
            # Step 4. Sort the right split array
            right = num[splitIndex+1:]
            right.sort()
            # Step 5. Combine the two arrays
            return num[0:splitIndex+1] + right


