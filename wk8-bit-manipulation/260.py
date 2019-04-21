class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a, b, c = 0, 0, 0

        for n in nums:
            c ^= n

        mask = c & (-c)
        for n in nums:
            if n & mask:
                a ^= n

        b = a ^ c

        return [a, b]
