class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candyArray = [1] * len(ratings)
        reNum = 1
        if len(ratings)>1:
            for i in range(len(ratings)):
                if i-1<0:
                    #check right
                    if ratings[i+1] < ratings[i]:
                        candyArray[i]=candyArray[i] +1
                elif i-1 >=0 and i<len(ratings)-1:
                    #check left
                    if ratings[i-1] < ratings[i] and ratings[i] > ratings[i+1]:
                        candyArray[i] = max(candyArray[i-1],candyArray[i+1])+1
                    elif ratings[i-1] < ratings[i]:
                        candyArray[i] = candyArray[i-1]+1
                    elif ratings[i+1] < ratings[i]:
                        candyArray[i] = candyArray[i+1]+1
                    #check right
                else:
                    if ratings[i-1] < ratings[i]:
                        candyArray[i] = candyArray[i-1]+1
            ratings.reverse()
            candyArray.reverse()
            for i in range(len(ratings)):
                if i-1<0:
                    #check right
                    if ratings[i+1] < ratings[i]:
                        candyArray[i]=candyArray[i+1] +1
                elif i-1 >=0 and i<len(ratings)-1:
                    #check left
                    if ratings[i-1] < ratings[i] and ratings[i] > ratings[i+1]:
                        candyArray[i] = max(candyArray[i-1],candyArray[i+1])+1
                    elif ratings[i-1] < ratings[i]:
                        candyArray[i] = candyArray[i-1]+1
                    elif ratings[i+1] < ratings[i]:
                        candyArray[i] = candyArray[i+1]+1
                    #check right
                else:
                    if ratings[i-1] < ratings[i]:
                        candyArray[i] = candyArray[i-1]+1

            reNum = sum(candyArray)
        return reNum
