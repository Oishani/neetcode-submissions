class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Get the number of rows and columns.
        ROWS, COLS = len(matrix), len(matrix[0])

        # Initialize the cache to be a hash map with (r, c) -> length of path.
        dp = {}

        # Inner DFS function passing the indices and previous value.
        def dfs(r, c, prev_val):
            # Base case 1: if indices are out of bounds or
            # if the current value is less or equal to the previous value, return 0.
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev_val:
                return 0
            # Base case 2: if the key is already in the cache, return the value.
            if (r, c) in dp:
                return dp[(r, c)]
            # Every number contributes at least 1 to the path length. Set 1 as the default result.
            res = 1
            # Then calculate how much the cells above, below, left, and right contribute to the result.
            # Update the result by take the max of the result so far and 1 + call to dfs for that cell.
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            # Cache the result and return it.
            dp[(r, c)] = res
            return res

        # Loop over the grid and
        for r in range(ROWS):
            for c in range(COLS):
                # call the recursive function on each grid value and previous value of -1.
                dfs(r, c, -1)
        # Return the max of the cached values.
        return max(dp.values())

# Time: O(m * n)
# Space: O(m * n)
        