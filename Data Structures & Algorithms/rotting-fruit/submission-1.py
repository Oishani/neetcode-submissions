class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        q = collections.deque()
        fresh = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc, in directions:
                    r = row + dr
                    c = col + dc

                    if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c))
            if q:
                time += 1

        return time if fresh == 0 else -1 

# Time: O(m * n)
# Space: O(m * n)