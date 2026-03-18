class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prev = [0] * (n + 1)

        ans = 0

        for i in range (1, m + 1):
            cur = [0] * (n + 1)
            row_prefix = 0
            for j in range(1, n + 1):
                row_prefix += grid[i - 1][j - 1]
                cur[j] = prev[j] + row_prefix

                if cur[j] <= k:
                    ans += 1
            prev = cur
        return ans