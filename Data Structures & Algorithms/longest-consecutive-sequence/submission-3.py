class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_ss = 0
        cur_ss = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_ss += 1
                while num + cur_ss in nums_set:
                    cur_ss += 1
                max_ss = max(max_ss, cur_ss)
                cur_ss = 0
        return max_ss