class Solution:

    def isInterleave(self,s1,s2,s3):
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        # Pretty smart
        last = set([(0,0)])

        for char in s3:
            current = set()
            for i, j in last:
                # Adding all the posibilities
                if i < l1 and s1[i] == char:
                    current.add((i+1,j))
                if j < l2 and s2[j] == char:
                    current.add((i,j+1))
            # If neither cases are true, ofcuz current will be null
            if not current:
                return False
            last = current
        return True
