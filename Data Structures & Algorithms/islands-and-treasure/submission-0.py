class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Get the dimensions of the grid.
        ROWS, COLS = len(grid), len(grid[0])
        # Initialize a directions list for horizontal and vertical neighbors.
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Initialize a deque.
        q = collections.deque()

        # Loop over grid and add all tresure chests to the deque.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Run multi-source BFS.
        # While deque is non-empty,
        while q:
            # Loop over the values in the deque.
            for i in range(len(q)):
                # Pop the treasure chest.
                row, col = q.popleft()
                # Loop over the directions and get the new positions.
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    # If the new positions are not within bounds or if it's not a land cell,
                    if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 2147483647:
                        # then continue.
                        continue
                    # Else, update the cell value to cell value of popped cell + 1. Then add the new cell to the deque.
                    grid[r][c] = grid[row][col] + 1
                    q.append((r, c))

        return

# Time: O(m * n)
# Space: O(m * n)
