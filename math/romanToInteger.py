class Solution:

    def romanToInt(self,s):
        romanDic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        toRet = 0
        lastChar = ''
        for char in s:
            if romanDic.get(lastChar):
                #4(IV),9(IX),40(XL),90(XC),400(CD),900(CM)
                if romanDic.get(lastChar) < romanDic[char]:
                    toRet = toRet + romanDic[char] - romanDic[lastChar]
                    #we erase the lastchar in this case
                    lastChar = ''
                else:
                    toRet = toRet + romanDic[lastChar]
                    lastChar = char
            else:
                lastChar = char

        #If the last case is like 4,9,40,90,400,900;
        #We already did the sumation. Else, we will have to add the last number
        if romanDic.get(lastChar):
            toRet = toRet + romanDic[lastChar]

        return toRet

