class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy brute force didnt work :(
        # what about normal brute force?
        maxProfit = prices[0] - prices[0]
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return maxProfit