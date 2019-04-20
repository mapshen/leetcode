from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses
        outdegree = defaultdict(list)
        order = []

        for succ, pre in prerequisites:
            indegree[succ] += 1
            outdegree[pre].append(succ)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            pre = q.popleft()
            order.append(pre)
            numCourses -= 1
            for succ in outdegree[pre]:
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    q.append(succ)

        if numCourses == 0:
            return order
        else:
            return []
