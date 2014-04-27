class Solution:
    # you can use a combination of array and table
    def convert(self, s, nRows):
        a = []
        dic = {}
        newStr = ""
        if nRows>1 and len(s)>nRows:
            for i in range(nRows):
                a.append(s[i])
                dic[s[i]] = []
            counter = 0
            direction = -1
            toAdd = nRows-1
            for i in range(nRows,len(s)):
                if counter < nRows -1:
                    toAdd = toAdd + direction
                    counter = counter +1
                    dic[a[toAdd]].append(s[i])
                else:
                    direction = direction * (-1)
                    toAdd = toAdd + direction
                    counter = 1
                    dic[a[toAdd]].append(s[i])
                    
            for i in range(len(a)):
                newStr = newStr+a[i] + "".join(dic[a[i]]).strip()
            return newStr
        else:
            return s
        
        
