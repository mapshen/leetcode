class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l=max(nums)
        r=sum(nums)
        n = len(nums)
        while l<r:
            mid = (r-l)//2+l
            sumsum=0
            count=0
            for i in range(n):
                sumsum += nums[i]
                if sumsum>mid:
                    sumsum=nums[i]
                    count+=1
                elif sumsum==mid:
                    sumsum=0
                    count +=1
            if sumsum!=0:
                count =count+1
            if count > m:
                l = mid+1
            else:
                r = mid
        return l
