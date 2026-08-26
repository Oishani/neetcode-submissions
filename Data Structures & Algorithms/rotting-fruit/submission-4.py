class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()

        directions = [(1, 0), (-1 , 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
            if q:
                time += 1
        
        return time if fresh == 0 else -1

# Time: O(m * n) where m is num of rows and n is num of columns
# Space: O(m * n)