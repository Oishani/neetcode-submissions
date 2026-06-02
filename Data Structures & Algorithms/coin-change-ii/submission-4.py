class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0 for a in range(amount + 1)] for c in range(len(coins) + 1)]

        for c in range(len(coins) + 1):
            dp[c][0] = 1

        for c in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[c]:
                    dp[c][a] += dp[c + 1][a] + dp[c][a - coins[c]]

        return dp[0][amount]

# Time: O(n * a)
# Space: O(n * a)