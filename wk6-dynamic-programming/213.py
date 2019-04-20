class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0

        if len(nums) <= 2:
            return max(nums)

        a, b, c, d = 0, 0, 0, 0

        for i in range(len(nums) - 1):
            a, b = b, max(b, a + nums[i])
            c, d = d, max(d, c + nums[i + 1])

        return max(a, b, c, d)
