# 207. Course Schedule
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for i in range(numCourses)]
        visit = [0]*numCourses
        for i in prerequisites:
            pre[i[0]].append(i[1])
        
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in pre[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

# 210. Course Schedule II
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visit = [0] * numCourses
        path = []
        
        def dfs(curr):
            if visit[curr] == 1:
                return False
            if visit[curr] == 2:
                return True
            visit[curr] = 1
            for j in graph[curr]:
                if not dfs(j):
                    return False
            visit[curr] = 2
            path.append(curr)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return path

# 802. Find Eventual Safe States
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visit = [0] * len(graph)
        res = []    
        
        def dfs(start):
            if visit[start] != 0:
                return visit[start] == 1
            visit[start] = 2
            for i in graph[start]:
                if not dfs(i):
                    return False
            visit[start] = 1
            return True
        
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
    


# 329. Longest Increasing Path in a Matrix
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in range(m)]
        
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0, 
                dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]
        return max(dfs(x, y) for x in range(m) for y in range(n))
