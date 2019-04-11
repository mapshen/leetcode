class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        vals = set(map(str, range(1, 10)))

        self.rows = [vals.copy() for _ in range(9)]
        self.cols = [vals.copy() for _ in range(9)]
        self.boxes = [vals.copy() for _ in range(9)]
        cells = []

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    cells.append((i, j))
                else:
                    self.rows[i].remove(num)
                    self.cols[j].remove(num)
                    self.boxes[i // 3 * 3 + j // 3].remove(num)

        def helper(idx, board):
            if idx == len(cells):
                return True

            i, j = cells[idx]

            nums = self.rows[i] & self.cols[j] & self.boxes[i // 3 * 3 + j // 3]

            for num in nums:
                self.rows[i].remove(num)
                self.cols[j].remove(num)
                self.boxes[i // 3 * 3 + j // 3].remove(num)
                board[i][j] = num

                if helper(idx + 1, board):
                    return True

                self.rows[i].add(num)
                self.cols[j].add(num)
                self.boxes[i // 3 * 3 + j // 3].add(num)

            return False

        helper(0, board)
