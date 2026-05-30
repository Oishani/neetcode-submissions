class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Get dimensions of the grid.
        ROWS, COLS = len(board), len(board[0])

        # Define inner DFS function that will flip current cell and it's neighbors to T
        # since we'll call this from the edge Os.
        def dfs(r, c):
            # If positions are out of bounds, or,
            # if the current cell is not an 0, do nothing
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            # Else, flip the cell to a T and call DFS on its 4 neighbors.
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Mark all Os along the edge to T. 
        # We'll flip them back to Os at the end because they can never be surrounded.
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
        for c in range(COLS):
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
        for r in range(ROWS):
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)

        # Loop over the grid. All remaining Os must be surrounded. Mark them as Xs.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # Flip the Ts back to Os.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

# Time: O(m * n)
# Space: O(m * n)
