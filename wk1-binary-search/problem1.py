class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        l=0
        r=len(nums)-1
        while l<=r:
            m = (r-l)//2+l
            print (l,m,r)
            if nums[m] == target:
                return True
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m]<nums[r]:
                if nums[r] >= target > nums[m]:
                    l = m+1
                else:
                    r = m-1
            else:
                r-=1
        return False

