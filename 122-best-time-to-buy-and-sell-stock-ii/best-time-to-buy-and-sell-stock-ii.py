from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        # Base case
        dp[0][1] = -prices[0]

        for i in range(1, n):
            # Update buy and sell states
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]






        