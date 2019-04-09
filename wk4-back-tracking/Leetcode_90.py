class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        def dfs(nums,temp,index):
            if index > len(nums):
                return 
            if temp not in result:
                result.append(temp)            
            for i in range(index,len(nums)):
                dfs(nums,temp+[nums[i]],i+1)
        dfs(nums,[],0)
        return result
