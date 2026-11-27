
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)

        dp = [0] * (budget + 1)

        for factor, price in items:
            count = 0

            for f, p in items:
                if f % factor == 0:
                    count += 1

            # 0/1 Knapsack
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + count)

        ans = 0

        for b in range(budget + 1):
            extra = (budget - b) // min_price
            ans = max(ans, dp[b] + extra)

        return ans
