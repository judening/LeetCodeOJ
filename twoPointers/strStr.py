class Solution:
    #O(mn) time complexity
    def strStr(self,haystack,needle):
        if len(needle) > len(haystack) or (needle and not haystack):
            return -1
        elif (not needle and not haystack) or (haystack and not needle):
            return 0
        else:
            j = 0
            i = 0

            while j < len(haystack):
                #The reason to set temp and i is because we might come back
                temp = j
                i = 0

                while i < len(needle):
                    #Be very cautious. It is possible that when you run out of the
                    #haystack (len(haystack[temp:]) < len(needle))
                    #That's why we need the first condition
                    if temp < len(haystack) and haystack[temp] == needle[i]:
                        i +=1
                        temp +=1
                        if i == len(needle):
                            return j
                    else:
                        j += 1
                        break
            return -1
