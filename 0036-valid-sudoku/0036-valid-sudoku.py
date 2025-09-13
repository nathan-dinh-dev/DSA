class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # declare sudoku size
        N = 9

        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # skip if val is NaN
                if val == ".":
                    continue
                
                # check if val is in the current rows or not
                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True 