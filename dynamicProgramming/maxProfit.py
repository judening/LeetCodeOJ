class Solution:

    #by keeping a minPrices' table,we always know what the minimum prices up till now
    def maxProfit(self,prices):
        if prices:
            minPrices = [prices[0]]
            profit = [0]
            for i in xrange(1,len(prices)):
                if prices[i] < minPrices[-1]:
                    minPrices.append(prices[i])
                    profit.append(0)
                else:
                    profit.append(prices[i]-minPrices[-1])
            return max(profit)
