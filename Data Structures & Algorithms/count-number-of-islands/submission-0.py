class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the dimensions of the grid.
        ROWS, COLS = len(grid), len(grid[0])
        # Initialize a visited set.
        visited = set()
        # Initialize a counter.
        count = 0

        # Define inner DFS function with current row and column passed in.
        def dfs(r, c):
            # If the positions are out of bounds or
            # if the current position has been visited or
            # if the current cell is water, return 0
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == "0":
                return 0
            # Else, mark this cell as visited and call DFS on all 4 neighbors.
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Loop over the grid.
        for r in range(ROWS):
            for c in range(COLS):
                # If this is an unvisited land cell, call DFS on it and increment the counter.
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        # Return the final count.
        return count

# Time: O(m * n)
# Space: O(m * n)
