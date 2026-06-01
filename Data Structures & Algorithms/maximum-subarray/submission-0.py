class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize a current sum  to 0 and a max sum to the first list value.
        cur_sum = 0
        max_sum = nums[0]

        # Loop over all the numbers.
        for n in nums:
            # If the current sum drops to negative, reset it to 0.
            if cur_sum < 0:
                cur_sum = 0
            # Otherwise, add the number to the current sum,
            cur_sum += n
            # update the max sum to be max of current sum and max sum.
            max_sum = max(cur_sum, max_sum)

        # Return max sum.
        return max_sum

# Time: O(n)
# Space: O(1)
        