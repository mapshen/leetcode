from collections import deque


class Solution:
    def breadth_first_search(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        queue = deque([click])
        visited = set([tuple(click)])
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1),
        ]

        while queue:

            for _ in range(len(queue)):
                x, y = queue.popleft()

                if board[x][y] == "M":
                    board[x][y] = "X"

                if board[x][y] == "E":
                    count = 0
                    neighbors = []

                    for direction in directions:
                        i, j = x + direction[0], y + direction[1]

                        if 0 <= i < m and 0 <= j < n:
                            if board[i][j] == "M":
                                count += 1
                            if board[i][j] == "E":
                                neighbors.append((i, j))

                    if count == 0:
                        board[x][y] = "B"
                        for neighbor in neighbors:
                            if neighbor not in visited:
                                visited.add(neighbor)
                                queue.append(neighbor)
                    else:
                        board[x][y] = str(count)

        return board

    def depth_first_search(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        stack = [click]
        visited = set([tuple(click)])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        while stack:
            x, y = stack.pop()

            if board[x][y] == "M":
                board[x][y] = "X"

            if board[x][y] == "E":
                count = 0
                neighbors = []

                for direction in directions:
                    i, j = x + direction[0], y + direction[1]
                    if 0 <= i < m and 0 <= j < n:

                        if board[i][j] == "M":
                            count += 1
                        if board[i][j] == "E":
                            neighbors.append((i, j))

                if count == 0:
                    board[x][y] = "B"
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                else:
                    board[x][y] = str(count)

        return board

