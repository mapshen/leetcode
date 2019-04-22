# 268. Missing numbers
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int(len(nums)*(len(nums) + 1)/ 2 - sum(nums))

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ (i^nums[i])
        return res

# 187. Repeated DNA Sequences
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 9:
            return []
        x = {}
        for i in range(len(s) - 9):
            if s[i : i + 10] in x:
                x[s[i:i + 10]] += 1
            else:
                x[s[i:i + 10]] = 1
        res = []
        for i in x:
            if x[i] > 1:
                res.append(i)
        return res
### bit manipulation
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1, n2 = 0, 0
        xor = 0
        for i in nums:
            xor ^= i
        x = 1
        while xor & x == 0:
            x = x << 1
        for i in nums:
            if i & x == 0:
                n1 ^= i
            else:
                n2 ^= i
        return [n1, n2]
