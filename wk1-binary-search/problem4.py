class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<r:
            m = (r-l)//2+l
            if nums[m] < nums[l]:
                r = m 
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        return nums[l]
