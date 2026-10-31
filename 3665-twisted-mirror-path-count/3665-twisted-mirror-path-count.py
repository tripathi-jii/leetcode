from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        def move(i, j, direction):
            # direction: 0 = Right, 1 = Down

            if direction == 0:
                j += 1
            else:
                i += 1

            while 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                if direction == 0:
                    i += 1
                    direction = 1
                else:
                    j += 1
                    direction = 0

            if 0 <= i < m and 0 <= j < n:
                return i, j

            return -1, -1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                if i == m - 1 and j == n - 1:
                    continue

                # Try moving right
                x, y = move(i, j, 0)
                if x != -1:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

                # Try moving down
                x, y = move(i, j, 1)
                if x != -1:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]