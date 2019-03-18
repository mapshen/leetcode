mport numpy as np
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i,j = np.where(np.array(grid) == 1)
        move = [[0,1],[0,-1],[1,0],[-1,0]]
        nr,nc = len(grid),len(grid[0])
        start = [int(i),int(j)]
        obs = sum(row.count(-1) for row in grid)
        
        
        def dfs(start,con,result,visited):
            result = result+[[start]]
            [r,c]=start
            visited = visited + [[r,c]]
            con = con + 1
            for dr,dc in move:
                tr = r+dr
                tc = c+dc
                
                if 0<=tr<nr and 0<=tc<nc :
                    if grid[tr][tc] == 0 and [tr,tc] not in visited:                 
                        dfs([tr,tc],con,result,visited)

                    if grid[tr][tc] == 2 and con ==nr*nc-1-obs:
                        out.append(result)
            return
        con = 0
        out=[]
        visited=[]
        dfs(start,con,[],visited)
        return len(out)
