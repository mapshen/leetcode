class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        def dfs(k,n,temp,index):
            if len(temp) > k:
                return
            if sum(temp) == n and (len(temp)) == k:
                result.append(temp)
                
            for i in range(index,9):
                dfs(k,n,temp+[i+1],i+1)
            
        dfs(k,n,[],0)
        return result
