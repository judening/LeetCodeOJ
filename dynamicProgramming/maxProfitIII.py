class Solution:
    # I honestly want myself to be that smart
    def maxProfit(self,prices):
        if prices:
            minPrices = [prices[0]]
            profitForward = [0]
            for i in xrange (1,len(prices)):
                if prices[i] < minPrices[-1]:
                    minPrices.append(prices[i])
                    profitForward.append(0)
                else:
                    profitForward.append(prices[i]-minPrices[-1])
            currentMax = 0
            maxProfit = 0
            # Max profit after i th day
            profitBackward = []
            for i in xrange(len(prices)-1,-1,-1):
                currentMax = max(prices[i],currentMax)
                maxProfit = max(maxProfit,currentMax-prices[i])
                profitBacward.insert(0,maxProfit+profitForward[i])
            return max(profitBackward)
        else:
            return 0
