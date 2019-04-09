class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=[]
        def check(x,y,temp):
            for [i,j] in temp:
                if i==x:
                    return False
                if j ==y:
                    return False
                if abs(i-x) == abs(j-y):
                    return False
            return True
        
        
        def dfs(n,temp,index):
            if index>n:
                return
            
            if index==n:
                result.append(temp)
                return
            
            for i in range(n):
                for j in range(n):
                    if check(i,j,temp) and i==index:
                        dfs(n,temp+[[i,j]],index+1)
            
        dfs(n,[],0)
        return len(result)
