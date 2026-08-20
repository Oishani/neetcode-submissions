class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        suf = 1

        prefix = []
        suffix = deque()

        result = []

        for i in range(len(nums)):
            prev_index = i - 1

            if prev_index < 0:
                prefix.append(pre)
            else:
                prefix_value = nums[prev_index] * pre
                prefix.append(prefix_value)
                pre = prefix_value

        for i in range(len(nums) - 1, -1, -1):
            next_index = i + 1

            if next_index >= len(nums):
                suffix.append(suf)
            else:
                suffix_value = nums[next_index] * suf
                suffix.appendleft(suffix_value)
                suf = suffix_value

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result

# Time: O(n) where n is len of nums
# Space: O(n)

        