class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        area = 0
        if not len(matrix):
            return area

        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[j] += 1
                else:
                    dp[j] = 0

            area = max(area, self.getLargestArea(dp))

        return area

    def getLargestArea(self, heights):
        area = 0
        length = len(heights)
        if not length:
            return area

        stack = [0]
        for i in range(1, length):
            while stack and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                if stack:
                    area = max(area, heights[j] * (i - stack[-1] - 1))
                else:
                    area = max(area, heights[j] * i)
            stack.append(i)

        while stack:
            j = stack.pop()
            if stack:
                area = max(area, heights[j] * (length - stack[-1] - 1))
            else:
                area = max(area, heights[j] * length)

        return area
