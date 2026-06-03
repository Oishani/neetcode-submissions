class Solution:
    def numDecodings(self, s: str) -> int:
        # Initialize a DP cache with a seed value of lebgth of string mappint to 1.
        # This is the base case: the empty string can be decoded in 1 way.
        dp = {len(s): 1}
        
        # Loop over the positions backwards.
        for i in range(len(s) - 1, -1, -1):
            # If the current character is a 0, then there are no ways to decode it. Cache 0 as the value.
            if s[i] == "0":
                dp[i] = 0
            # Otherwise, there's always 1 way to decode it - take 1 digit.
            else:
                dp[i] = dp[i + 1]
            # If there's a next character within range and if the current character starts with 1, or
            # if the current character starts with 2 and the next character is a digit in the range 0-6,
            if (i + 1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                # then there's two ways to decode it - take 2 characters and add it to the current cached value.
                dp[i] += dp[i + 2]

        # Return cached value at 0.
        return dp[0]

# Time: O(n)
# Space: O(n)
