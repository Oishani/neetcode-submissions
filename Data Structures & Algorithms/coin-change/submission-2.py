class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a DP cache for every target till amount + 1 with a value of amount + 1.
        # The cache stores amount -> min coins 
        dp = [amount + 1] * (amount + 1)
        # Minimum coins to make target 0 is 0.
        dp[0] = 0

        # Since target 0 is settled, loop over from target 1 up and including amount.
        for a in range(1, amount + 1):
            # Nested loop over all coins.
            for c in coins:
                # If the current target is >= the current coin value, then,
                if a >= c:
                # the minimum coins to make target a is min of 
                # cached value of a (not taking current coin) and 1 + cached value of target excluding current coin (taking current coin). 
                    dp[a] = min(dp[a], 1 + dp[a - c])


        # Return the cache value of amount if it's not the initial value, else return -1.
        return dp[amount] if dp[amount] != (amount + 1) else -1 

# Time: O(a * c)
# Space: O(a)