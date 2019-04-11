class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.positions = []

        def backtrack(idx):
            if len(self.positions) == n:
                self.count += 1

            for j in range(n):
                if self._is_attacked(idx, j):
                    continue

                self.positions.append((idx, j))
                backtrack(idx + 1)
                self.positions.pop()

        backtrack(0)
        return self.count

    def _is_attacked(self, i, j):
        for x, y in self.positions:
            if i == x \
                    or j == y \
                    or i - j == x - y \
                    or i + j == x + y:
                return True
        return False
