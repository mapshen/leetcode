class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        minp = maxp = ans = nums[0]

        for i in range(1, len(nums)):
            pre_minp, pre_maxp = minp, maxp
            maxp = max(pre_maxp * nums[i], pre_minp * nums[i], nums[i])
            minp = min(pre_maxp * nums[i], pre_minp * nums[i], nums[i])

            ans = max(maxp, ans)
        return ans
