class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxSum = nums[0]
        curSum = 0

        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = max(curSum, maxSum)

        return maxSum

# Time: O(n) where n is len of nums
# Space: O(1)


        