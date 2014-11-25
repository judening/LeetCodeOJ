# Best time to buy and sell stock II
# The ith element is the price of *a given stock* on day i
# I can complete as many transactions as I like,but I have to finish
# a transaction before I start another one.

# Question to think about after reading the ridiculously easy solution
# Why buying on day i and selling it on day i+1 if p[i+1] > p[i] guarantees
# optimality?

# 1).If you buy on day i and sell it on day j (i<j), you may not make the
# greatest profit *during that time window*, as there might be day k(i<k<j)
# where p[k]>p[j]. So you need to sell it earlier

# 2).If you buy on day i and sell it on day j (i<j), you may not make the
# greatest profit *possible with that stock* because there might be day
# k (i<k<j) where p[k]>p[j], you are better off just sell it on day k

# -1.To avoid 1), we should do capture the differences once p[i+1]>p[i]. This
# ensure that you won't miss the day k mention above in 1)

# -2.To avoid 2), which we already did, since with the condition given, we
# would end up with getting the optimal result. Let's say day p[j]>p[k].
# Total profit = p[j]-p[k] + p[k]-p[i] = p[j]-p[i], which is essentially
# the same

class Solution:
    def maxProfit(self,prices):
        int p = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                p = p + prices[i] - prices[i-1]

        return p

