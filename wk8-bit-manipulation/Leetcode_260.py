class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all_num = 0
        for num in nums:
            all_num^=num
        
        a=all_num
        b=all_num
        
        mask = all_num&(-all_num)
        
        for num in nums:
            if (mask&num):
                a^=num
            else:
                b^=num
        return [a,b]
            
