class Solution:

    #Caveats: 1. Remember to concatenate the string
    #         2. Remember to minus 5 when the digit is >4 and <9
    def intToRoman(self,num):
        dicArray = [['I','V'],['X','L'],['C','D'],['M']]
        counter = 0
        toRet = ''
        while num > 0:
            lastDigit = num%10
            if lastDigit>0 and lastDigit<4:
                toRet = lastDigit*dicArray[counter][0] + toRet
            elif lastDigit == 4:
                toRet = dicArray[counter][0] + dicArray[counter][1] + toRet
            elif lastDigit >4 and lastDigit<9:
                toRet = dicArray[counter][1] + (lastDigit-5)*dicArray[counter][0] + toRet
            elif lastDigit == 9:
                toRet = dicArray[counter][0] + dicarray[counter+1][0] + toRet

            counter = counter+1
            num = num/10
        return toRet
