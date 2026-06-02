class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        output = []
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean, prev_height):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in ocean or heights[r][c] < prev_height:
                return
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
            

        for c in range(COLS):
            dfs(0, c, pacific, 0)

        for r in range(ROWS):
            dfs(r, 0, pacific, 0)

        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, 0)

        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, 0)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    output.append([r, c])

        return output

# Time: O(m * n)
# Space: O(m * n)