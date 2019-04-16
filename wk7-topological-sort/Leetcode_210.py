collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        def dfs(node,out_code,in_code,result):
            in_code[node]=1
            
            for child in out_code[node]:
                if in_code[child] == 0:
                    if not dfs(child,out_code,in_code,result):
                        return False
                elif in_code[child] == 1:
                    return False
                elif in_code[child]==2:
                    pass
            in_code[node]=2
            result.appendleft(node)
            return True
        
        out_code=[[] for _ in range(numCourses)]
        in_code = [0 for _ in range(numCourses)]
        
        for edge in prerequisites:
            out_code[edge[1]].append(edge[0])

        result=deque([])
        
        for i in range(numCourses):
            if in_code[i] ==0:
                if not dfs(i,out_code,in_code,result):
                    return []
        return result
            
