class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Let the goal be set to the last index.
        goal = len(nums) - 1

        # Loop over the number backwards from second last.
        for i in range(len(nums) - 2, -1 , -1):
            # If the current index + the value at it can reach or exceed the goal, reset the goal to the current index.
            if i + nums[i] >= goal:
                goal = i

        # Return whether goal is at index 0 or not.
        return goal == 0

# Time: O(n)
# Space: O(1)
        