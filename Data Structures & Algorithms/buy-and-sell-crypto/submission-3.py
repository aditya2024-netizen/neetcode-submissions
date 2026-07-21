class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            
            curr_profit = price - minimum_price
            if curr_profit > max_profit:
                max_profit = curr_profit
            
        return max_profit
            
