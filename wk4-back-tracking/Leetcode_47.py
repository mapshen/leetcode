class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        
        
        result=[]
        def dfs(temp):
            if temp in result:
                return
            if temp not in result:
                result.append(temp)
            for i in range(0,len(temp)-1):
                for j in range(i+1,len(temp)):
                    dfs(temp[:i]+[temp[j]]+temp[i+1:j] + [temp[i]] +temp[j+1:])
        
        dfs(nums)
        return result
