class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        self.powerset = []

        def helper(subset, idx):
            if subset not in self.powerset:
                self.powerset.append(subset)

            for i in range(idx + 1, size):
                helper(subset + [nums[i]], i)

        helper([], -1)
        return self.powerset
