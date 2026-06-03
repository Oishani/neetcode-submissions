class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Take neutral values to multiply the current max and the current min with.
        cur_max, cur_min = 1, 1
        # Let result be initialized to the first number.
        res = nums[0]

        # Loop over all the numbers.
        for n in nums:
            # Store the product of current max and current number in a temp var to reuse for updating current min.
            temp = n * cur_max
            # Update the current max to be max of current max multiplied by the current number,
            # current min multiplied by the current number, and the number itself.
            cur_max = max(n * cur_max, n * cur_min, n)
            # Update the current min similarly (take min).
            cur_min = min(n * cur_min, temp, n)
            # Update result to be the max of itself and current max
            res = max(res, cur_max)
        # Return the result.
        return res
# Time: O(n)
# Space: O(1)