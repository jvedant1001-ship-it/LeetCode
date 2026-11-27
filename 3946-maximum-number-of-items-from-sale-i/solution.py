from typing import List
from math import inf

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # dp[j] stores the max items obtained by spending at most j on first purchases
        dp = [0] * (budget + 1)
        min_price = inf
        
        for factor, price in items:
            # Update the global minimum price for the final step
            min_price = min(min_price, price)
            
            # Calculate value: count of items whose factor is divisible by current factor
            # This includes the item itself + all free items it unlocks
            value = sum(1 for f, _ in items if f % factor == 0)
            
            # 0-1 Knapsack transition: iterate backwards to avoid reusing the same item
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + value)
        
        # Combine DP result with spending leftover budget on the cheapest item
        max_items = 0
        for i in range(budget + 1):
            remaining_budget = budget - i
            extra_items = remaining_budget // min_price
            max_items = max(max_items, dp[i] + extra_items)
            
        return max_items
