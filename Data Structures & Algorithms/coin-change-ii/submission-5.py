class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize cache to be inclusive of amount. 
        dp = [0] * (amount + 1)
        # Initialize first value: Only 1 way to reach target 0.
        dp[0] = 1

        # Loop over all coins.
        for coin in coins:
            # Loop over all amounts in current coin value to target amount (inclusive).
            for a in range(coin, amount + 1):
                # Update the cache: number of ways to reach current amount without this coin + number of ways to reach amount - coin.
                dp[a] += dp[a - coin]

        # Return the cached value for the target amount.
        return dp[amount]

# Time: O(n * amount)
# Space: O(amount)
