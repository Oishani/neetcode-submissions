class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the grid.
        ROWS, COLS = len(heights), len(heights[0])
        # Initialize the output list.
        output = []
        # Initialize two ocean sets to record which cells can flow to them.
        pacific = set()
        atlantic = set()

        # Define an inner DFS function with row, col, ocean set, and height of previous cell.
        def dfs(r, c, ocean, prev_height):
            # Check whether row and col are out of bounds, or
            # the cell is already in the ocean's set, or
            # the current cell's height is lower than the previous cell's height.
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in ocean or heights[r][c] < prev_height:
                # If yes, return nothing.
                return
            # If not, add the current cell's position to the ocean's set.
            ocean.add((r, c))
            # Call DFS on current cell's 4 neighbors.
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
        
        # From all the top and left edge cells call DFS on the current cell with previous height 0 and ocean set pacific.
        for c in range(COLS):
            dfs(0, c, pacific, 0)
        for r in range(ROWS):
            dfs(r, 0, pacific, 0)

        # From all the bottom and right edge cells call DFS on the current cell with previous height 0 and ocean set atlantic.
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, 0)
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, 0)

        # Loop over the entire grid and add all cells that are
        # in both the pacific and atlantic sets to the output.
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    output.append([r, c])

        # Return the output.
        return output

# Time: O(m * n)
# Space: O(m * n)