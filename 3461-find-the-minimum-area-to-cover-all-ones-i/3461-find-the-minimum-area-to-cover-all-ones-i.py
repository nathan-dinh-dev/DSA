class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)

        min_row, max_row = rows, 0
        min_col, max_col = cols, 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_row = min(min_row, row)
                    max_row = max(max_row, row)
                    min_col = min(min_col, col)
                    max_col = max(max_col, col)
        
        return (max_col - min_col + 1) * (max_row - min_row + 1)