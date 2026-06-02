class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for n in nums:
            new_dp = defaultdict(int)
            for t, ways in dp.items():
                new_dp[t - n] += ways
                new_dp[t + n] += ways
            dp = new_dp

        return dp[target]

# Time: O(n * m) where m is sum of all nums
# Space: O(m)