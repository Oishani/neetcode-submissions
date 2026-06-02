class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # Store the number of stairs as the length of the cost list.
        # n = len(cost)
        # # The min cost from stairs n - 1 and n - 2 are the values at those indices. We don't need to calculate them.
        # # Loop backwards from the third last stair.
        # for i in range(n - 3, -1, -1):
        #     # The min cost at each stair is the min of the cost at that stair plus
        #     # the min costs of the 2 stairs ahead of it.
        #     cost[i] += min(cost[i + 1], cost[i + 2])

        # # Finally, return the min of the values stored at stairs 0 and 1 since we can start from either.
        # return min(cost[0], cost[1])

# Time: O(n)
# Space: O(1)

        # Store the number of stairs as the length of the cost list.
        n = len(cost)
        # Initialize a DP cache to store stair -> min cost.
        dp = [0] * (n + 1)

        # Loop over the stairs from stair 2 up to and including n.
        for i in range(2, n + 1):
            # The min cost at the current stair is the min of the cost of the two stairs before it.
            # We must pay the cost at each of those 2 indices.
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # At the end, return the value stored at the nth stair.
        return dp[n]

# Time: O(n)
# Space: O(n)