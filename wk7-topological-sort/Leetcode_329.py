class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        def dfs(x,y):
            #print result,x,y
            if not result[x][y]:
                result[x][y] = 1+ max(
                dfs(x-1,y) if x>0 and matrix[x-1][y] <matrix[x][y] else 0,
                dfs(x+1,y) if x<n-1 and matrix[x+1][y] <matrix[x][y] else 0,
                dfs(x,y-1) if y>0 and matrix[x][y-1] <matrix[x][y] else 0,
                dfs(x,y+1) if y<m-1 and matrix[x][y+1] <matrix[x][y] else 0
                )
            return result[x][y]
        
        if not matrix:
            return 0
        
        n,m=len(matrix),len(matrix[0])
        result=[[0 for _ in range(m)] for __ in range(n)]
        return max(dfs(x,y) for x in range(n) for y in range(m))
