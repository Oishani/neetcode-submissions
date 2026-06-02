class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there are no houses, return 0.
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # Return the max from robbing all but the first house and all but the last house.
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        # Get the number of houses as the length of the nums array.
        n = len(nums)

        # If there are no houses, return 0.
        if not nums:
            return 0
        # If there's just 1 house, return the money in that house.
        if n == 1:
            return nums[0]
        # Initialize a DP cache to store house -> max money.
        dp = [0] * n

        # Max value for house 0 is just the money at house 0.
        dp[0] = nums[0]
        # Max value for house 1 is the max of house 0 and 1.
        dp[1] = max(nums[0], nums[1])

        # Loop from house 2.
        for i in range(2, n):
            # The max at each house is max of the amount from not robbing the house (same as i - 1)
            # or from robbing the house (amount at current house and the amount from house i - 2)
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        # Return the last item in the cache.
        return dp[n-1]

# Time: O(n)
# Space: O(n)
