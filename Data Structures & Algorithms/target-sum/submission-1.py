class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Initialize the cache to a defaultdict. Cache is target -> ways to build target
        dp = defaultdict(int)
        # Base case: there is 1 way to get to a target of 0.
        dp[0] = 1

        # Loop over all nums
        for num in nums:
            # Initialize a new cache
            new_dp = defaultdict(int)
            # Loop over all items in the original cache.
            for t, ways in dp.items():
                # Update the new cache:
                # build up the target by adding or subtracting the current number and cumulating the number of ways.
                new_dp[t + num] += ways
                new_dp[t - num] += ways
            # Re-assign cache.
            dp = new_dp
        # Return cahched value for target.
        return dp[target]

# Time: O(n * m) where m is sum of all nums
# Space: O(m)