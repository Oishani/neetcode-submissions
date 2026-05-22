class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize a cache as a 2D grid with all inifities.
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # Initialize the right-most column and bottom-most row by the nuber of operations
        # it would take to convert each substring.
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # Loop over grid bottom-up.
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # If the characters in both positions are equal,
                if word1[i] == word2[j]:
                    # Cache the min operations needed to be 0.
                    dp[i][j] = dp[i + 1][j + 1]
                # If the character arew not equal,
                else:
                    # cache the value to be 1 + the minimum of all 3 decisions.
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        # Return the value in the top-left.
        return dp[0][0]

# Time: O(m * n)
# Space: O(m * n)



