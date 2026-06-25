class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy brute force didnt work :(
        # - important test case
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP