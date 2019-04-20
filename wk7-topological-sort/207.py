from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
