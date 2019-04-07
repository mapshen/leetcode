class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        total = 0
        self.count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(R):
            for c in range(C):
                if grid[r][c] != -1: total += 1
                if grid[r][c] == 1: sr, sc = r, c
                if grid[r][c] == 2: tr, tc = r, c

        def helper(r, c, total):
            total -= 1
            if total < 0: return
            if r == tr and c == tc and total == 0:
                self.count += 1
                return

            grid[r][c] = -1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    helper(nr, nc, total)
            grid[r][c] = 0

        helper(sr, sc, total)
        return self.count