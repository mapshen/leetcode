class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def dfs(node,in_node,out_node):
            in_node[node]=1
            for child in out_node[node]:
                if in_node[child] ==0:
                    if not dfs(child,in_node,out_node):
                        return False
                elif in_node[child]==1:
                    return False
                elif in_node[child]==2:
                    pass
            in_node[node]=2
            result.append(node)
            return True
        
        in_node=[0 for _ in range(len(graph))]
        out_node = graph
        
        result = []
        for i in range(len(graph)):
            if in_node[i] ==0:
                dfs(i,in_node,out_node)

        result.sort()
        return result
        
