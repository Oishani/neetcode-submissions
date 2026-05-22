class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Base case: return True if length of s3 not = length of s1 + s2.
        if len(s3) != len(s1) + len(s2):
            return False

        # Initialize the 2D cache for len + 1 of both strings. All values False.
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # The bottom-right corner value will be True.
        dp[len(s1)][len(s2)] = True

        # Loop over matrix from bottom-right to top-left.
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # Check 3 conditions for s1:
                # 1. if i is in range, 
                # 2. if the target character at s3 is the current target character,
                # 3. if the grid value below is a True value.
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    # Cache the value of this computation as True.
                    dp[i][j] = True

                # Check 3 conditions for s2:
                # 1. if j is in range, 
                # 2. if the target character at s3 is the current target character,
                # 3. if the grid value to the right is a True value.
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    # Cache the value of this computation as True.
                    dp[i][j] = True
        # Return value in top-left.
        return dp[0][0]

# Time: O(m * n)
# Space: O(m * n)


        