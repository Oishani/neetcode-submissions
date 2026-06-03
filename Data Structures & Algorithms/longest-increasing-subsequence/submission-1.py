class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize a DP cache storing num -> max LIS. 
        # Every numer is an LIS of length 1 so initial vale should be 1.
        LIS = [1] * len(nums)

        # Loop backwards from length - 1.
        for i in range(len(nums) - 1, -1, -1):
            # Nested for loop to iterate from i + 1 to length of nums.
            for j in range(i + 1, len(nums)):
                # If the next element (at j) is strictly greater than the previous element (at i),
                if nums[j] > nums[i]:
                    # then the LIS at i is the max of itself and 1 + LIS at j since we're adding the current num to the LIS.
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # Return the max stored value in the cache.
        return max(LIS)

# Time: O(n^2)
# Space: O(n)