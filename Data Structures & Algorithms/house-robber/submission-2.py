class Solution:
    def rob(self, nums: List[int]) -> int:
        # Get the numbr of houses at the length of the nums array.
        n = len(nums)

        # If there are no houses, return 0
        if not nums:
            return 0
        # If there's just 1 house, return the money in that house.
        if n == 1:
            return nums[0]
        # Initialize a DP cache to store house -> max money.
        dp = [0] * n

        # Max value for house 

        for i in range(n):
            dp[i] += max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n-1]
