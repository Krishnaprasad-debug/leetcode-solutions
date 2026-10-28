class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[False] * 1024 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                cur = [False] * 1024

                if i == 0 and j == 0:
                    cur[val] = True
                else:
                    if i > 0:
                        for x in range(1024):
                            if dp[j][x]:
                                cur[x ^ val] = True

                    if j > 0:
                        for x in range(1024):
                            if dp[j - 1][x]:
                                cur[x ^ val] = True

                dp[j] = cur

        return next(x for x in range(1024) if dp[n - 1][x])
