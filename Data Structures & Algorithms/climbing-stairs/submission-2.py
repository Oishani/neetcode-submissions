class Solution:
    def climbStairs(self, n: int) -> int:
        # # Initialize the first step (one) and the previous step (two) to 1 ways to get there.
        # one, two = 1, 1

        # # Run a loop till 1 less step since the first step is already initiliazed.
        # for i in range(n - 1):
        #     # Keep adding one and two as you progress.
        #     temp = one
        #     one = one + two
        #     two = temp
        # # Return the value of the current stair.
        # return one
        
# Time: O(n)
# Space: O(1)

        # If there are 2 or fewer stairs, the number of ways = number of stairs.
        if n <=2:
            return n
        # Initialize a DP cache that stores stair -> distinct ways.
        dp = [0] * (n+1)
        # There's 1 way to get to stair 1 and 2 ways to get to stair 2.
        dp[1], dp[2] = 1, 2

        # Loop over stair 3 up to and including n.
        for i in range(3, n+1):
            # At each stair, the number of distinct ways = the sum of the ways of the 2 stairs before it.
            dp[i] = dp[i - 1] + dp[i - 2]
        # Return the cached value at n.
        return dp[n]

# Time: O(n)
# Space: O(n)