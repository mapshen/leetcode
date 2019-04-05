class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        min_nums=nums[0]
        max_nums=nums[0]
        max_ans = nums[0]
        
        for num in nums[1:]:
            min_nums,max_nums = min(num,num*min_nums,num*max_nums),max(num,num*min_nums,num*max_nums)
            if max_nums > max_ans:
                max_ans = max_nums
        return max_ans
