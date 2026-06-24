class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l= 0
        r=1
        best_profit = 0
        while r < len(prices) :
            if prices[r] < prices[l] :
                l = r
                r+=1
                continue
            elif prices[r] >= prices[l] :
                if prices[r] - prices[l] > best_profit:
                    best_profit = prices[r] - prices[l]
                r += 1

        return best_profit