class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        r,nr,rf,nrf=nums[0],0,0,0
        
        for num in nums[1:]:
            r,nr = nr+num,max(r,nr)
            rf,nrf = nrf+num,max(rf,nrf)
            
        return max(nr,rf,nrf)
