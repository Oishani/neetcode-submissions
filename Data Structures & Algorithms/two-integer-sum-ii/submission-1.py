class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize a left and right pointer at the first and last indices.
        l, r = 0, len(numbers) - 1

        # Run a while loop while l < r.
        while l < r:
            # Store a sum of the numbers at both pointers.
            s = numbers[l] + numbers[r]

            # If the sum is larger than the target, decrement the right pointer.
            if s > target:
                r -= 1
            # If the sum is smaller than the target, increment the left pointer.
            elif s < target:
                l += 1
            # Otherwise, we've found our indices. Return the 1-indexed values of the pointers as an array.
            else:
                return [l + 1, r + 1]

# Time: O(n)
# Space: O(1)