class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get dimensions of grid.
        ROWS, COLS = len(grid), len(grid[0])
        # Initialize a visited set.
        visited = set()
        # Initialize area to 0.
        area = 0

        # Define inner DFS function with row and column value passed in.
        def dfs(r, c):
            # If the positions are out of bounds or
            # if the current position has been visited or
            # if the current position is water return 0.
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            # Else, mark this position as visited and call DFS on the horizontal and vertical neighbors while adding 1 to the area and summing the calls.
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


        # Loop over grid.
        for r in range(ROWS):
            for c in range(COLS):
                # Take max of current area and result of calling DFS on the current position.
                area = max(area, dfs(r, c))

        # Return area.
        return area

# Time: O(m * n)
# Space: O(m * n)