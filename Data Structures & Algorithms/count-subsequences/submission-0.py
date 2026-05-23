class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Initialize the cache to a hash map of (s index, t index) -> number of subsequences.
        dp = {}

        # Base case: if the length of the target string is greater than the length of the given string, return 0.
        if len(t) > len(s):
            return 0

        # Inner DFS function with the indices as params.
        def dfs(i, j):
            # Base case 1: if index of target string goes out of bounds (target string empty), return 1 (1 distinct subsequence).
            if j >= len(t):
                return 1
            # Base case 1: if index of given string goes out of bounds, return 0.
            if i >= len(s):
                return 0
            # Base case 3: If the key is already cached. return the value.
            if (i, j) in dp:
                return dp[(i, j)]

            # If the characters at the indices match, then 
            # take sum of moving onto the next characters or moving onto the next character in the given string but staying on the same character for the target string. 
            # Cache the result.
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            # If they don't match, just move onto to the next character of the given string.
            else:
                dp[(i, j)] = dfs(i + 1, j)
            # Return the cached value.
            return dp[(i, j)]
        
        # Trigger recursion starting at the first indices.
        return dfs(0, 0)

# Time: O(m * n)
# Space: O(m * n)
            
            
        