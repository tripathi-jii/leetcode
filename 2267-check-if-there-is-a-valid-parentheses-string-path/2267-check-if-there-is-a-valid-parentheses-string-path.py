class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] != '(' or grid[m - 1][n - 1] != ')':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                balances = set()

                if i > 0:
                    balances.update(dp[i - 1][j])

                if j > 0:
                    balances.update(dp[i][j - 1])

                for balance in balances:
                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]