from typing import List

"""
This sol works because:
- Two pointers l and r are already condition to be l < r always
- Pointer l is always the smallest possible value seen until r because it will be updated as soon 
as it find another smaller value. 
- Note to initialize maxProfit to be 0 (not -1 or so) because it will be the return when there is 
no profitable result in the given sequence. 

Time O(n) 
Space O(1) only need to store a fixed number of extra variables
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # left: buy, right: sell
        maxProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
