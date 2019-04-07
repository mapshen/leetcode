from collections import defaultdict, deque


class Solution:
    def DFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        status = [-1] * numCourses
        mapping = defaultdict(list)

        for succ, pre in prerequisites:
            mapping[pre].append(succ)

        def helper(pre):
            status[pre] = 0

            for succ in mapping[pre]:
                if status[succ] == -1:
                    if not helper(succ):
                        return False
                if status[succ] == 0:
                    return False

            status[pre] = 1
            return True

        for pre in range(numCourses):
            if status[pre] == -1:
                if not helper(pre):
                    return False
        return True


class Solution:
    def BFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        outdegree = defaultdict(list)

        for succ, pre in prerequisites:
            indegree[succ] += 1
            outdegree[pre].append(succ)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            pre = q.popleft()
            numCourses -= 1
            for succ in outdegree[pre]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    q.append(succ)

        return numCourses == 0