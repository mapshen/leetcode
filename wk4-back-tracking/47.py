class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        self.temp = []
        size = len(nums)
        self.visited = [0] * size

        def helper():
            duplicate = -1
            for i in range(size):
                if self.visited[i] == 1:
                    continue

                if duplicate >= 0 and nums[i] == nums[duplicate]:
                    continue

                self.temp.append(nums[i])
                self.visited[i] = 1

                if len(self.temp) == size:
                    self.permutations.append(self.temp[:])
                else:
                    helper()

                self.temp.pop()
                self.visited[i] = 0
                duplicate = i

        nums.sort()
        helper()
        return self.permutations
