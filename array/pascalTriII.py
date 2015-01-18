class Solution:

    def getRow(self,rowIndex):
        row = [1]
        i = 0
        while i<rowIndex:
            j = 0
            temp = 0
            popTimes = len(row)
            while j < popTimes:
                row.append(temp+row[0])
                temp = row.pop(0)
                j+=1
            row.append(temp)
            i+=1
        return row
