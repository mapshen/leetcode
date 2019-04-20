from collections import defaultdict, deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        indegree = [0] * len(graph)
        outdegree = defaultdict(list)
        result = []

        for i, g in enumerate(graph):
            for j in g:
                indegree[i] += 1
                outdegree[j].append(i)

        q = deque()
        for i in range(len(graph)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            result.append(node)
            for i in outdegree[node]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

        return sorted(result)