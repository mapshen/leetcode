class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = len(nums) - k
        left, right = 0, len(nums) - 1

        while True:
            pos = self.partition(left, right, nums)
            print(pos)
            if pos == kth:
                return nums[pos]
            elif pos > kth:
                right = pos - 1
            else:
                left = pos + 1

    def partition(self, left, right, nums):
        pivot = nums[right]
        l, r = left, right - 1

        while l <= r:
            if nums[l] > pivot and nums[r] < pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] <= pivot:
                l += 1
            if nums[r] >= pivot:
                r -= 1

        nums[right], nums[l] = nums[l], nums[right]

        return l
