class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        self.dp = [[0 for i in range(n)] for j in range(m)]

        def helper(i, j):
            if not self.dp[i][j]:
                self.dp[i][j] = 1 + max([
                    helper(i + x, j + y) \
                        if 0 <= i + x < m \
                           and 0 <= j + y < n \
                           and matrix[i][j] > matrix[i + x][j + y] \
                        else 0 \
                    for x, y in directions
                ])

            return self.dp[i][j]

        return max(helper(i, j) for j in range(n) for i in range(m))
