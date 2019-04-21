class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        a, b = nums[0], 0

        for i in range(1, len(nums)):
            a ^= nums[i]
            b ^= i

        return a ^ b ^ len(nums)
