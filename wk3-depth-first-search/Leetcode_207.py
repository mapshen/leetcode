class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        course_dict = collections.defaultdict(set)
        for i,j in prerequisites:
            course_dict[i].add(j)
        
        color = [0] * numCourses
        
        def dfs(u):
            if color[u] == 0:
                color[u] = 1
                for v in course_dict[u]:
                    if color[v]==1:
                        return False
                    else:
                        if not dfs(v):
                            return False
                color[u] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
