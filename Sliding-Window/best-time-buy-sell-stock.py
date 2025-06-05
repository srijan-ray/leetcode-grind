from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) <= 1):
            return 0
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
        
        return maxProfit
