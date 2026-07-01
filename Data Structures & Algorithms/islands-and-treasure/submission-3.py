class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 2147483647:
                        continue
                    grid[r][c] = grid[row][col] + 1
                    q.append((r, c))

        # Time: O(m * n)
        # Space: O(m * n)

