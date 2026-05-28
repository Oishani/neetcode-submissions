class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid.
        ROWS, COLS = len(grid), len(grid[0])
        # Initialize the time and number of fresh fruits to 0.
        mins, fresh = 0, 0
        # Initialize a deque.
        q = collections.deque()
        # Initialize a directions array.
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Count the number of fresh fruits by looping over the grid
        # and add all rotten fruits to the deque.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        # Run multi-source BFS on all rotten fruits.
        # While the deque is non-empty,
        while q:
            # run a loop over the length of the deque. 
            for i in range(len(q)):
                # Pop the first item in the deque.
                r, c = q.popleft()
                # Loop over the directions, store the new row and col values,
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    # check if the new row and col values are out of bounds or if the value is not a fresh fruit. If so, continue.
                    if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                        continue
                    # Else, mark the grid position as rotten, decrement the fresh fruit count, and append the position to the deque.
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))
            # In the outer for loop, only increment the number of mins if there are any rotten fruits in the deque.
            if q:
                mins += 1
        # Return the number of mins if there are 0 fresh fruits, else return -1.
        return mins if fresh == 0 else -1

# Time: O(m * n)
# Space: O(m * n)


        


        