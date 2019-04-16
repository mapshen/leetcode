class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_code=[0 for _ in range(numCourses)]
        out_code = [[] for _ in range(numCourses)]

        for edge in prerequisites:
            node1,node2=edge[0],edge[1]
            in_code[node1] +=1
            out_code[node2].append(node1)
            
        queue = [i for i,x in enumerate(in_code) if x==0]
        index = 0
        while queue:
            cur_node = queue.pop(0)
            index +=1
            for child in out_code[cur_node]:
                in_code[child] -= 1
                if in_code[child] == 0:
                    queue.append(child)
        if index == numCourses:
            return True
        return False
