# 81 Search in Rotated Sorted Array II
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) <= 1:
            if len(nums) == 0:
                return False
            else:
                return True if nums[0] == target else False

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2
            if target == nums[mid]:
                return True
            else:
                if nums[mid] > nums[low]: # low to mid sorted
                    if target >= nums[low] and target < nums[mid]:
                        high = mid - 1
                    else:
                        low =  mid + 1
                elif nums[mid] < nums[low]: # mid to high sorted
                    if target > nums[mid] and target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    low = low + 1
        return False

# 278  First Bad Version
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        low = 1
        high = n
        mid = low + (high - low)//2
        while(mid != low):
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
            mid = low + (high - low)//2
        return high

# 744. Find Smallest Letter Greater Than Target
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        mid = low + (high - low)//2
        while low < high:
            if letters[mid] > target:
                high = mid
            elif letters[mid] <= target:
                low = mid + 1
            mid = low + (high - low)//2
        return letters[high] if letters[high] > target else letters[0]


# 153. Find Minimum in Rotated Sorted Array
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        low = 0
        high = len(nums) - 1
        mid = low + (high - low)//2

        while 1:
            if low == mid:
                return nums[high] if nums[high] < nums[low] else nums[low]

            if nums[low] > nums[high]:
                if nums[low] > nums[mid]:
                    if nums[mid] > nums[mid - 1]:
                        high = mid - 1
                    else:
                        return nums[mid]
                else:
                    #nums[low] < nums[mid]
                    if nums[mid] < nums[mid+1]:
                        low = mid + 1
                    else:
                        return nums[mid + 1]
                mid = low + (high - low)//2
            else:
                return nums[low]


# 378 Kth Smallest Element in a Sorted Matrix
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        while low < high:
            mid = low + (high - low)//2
            count = self.count_lower_than_mid(matrix, n, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low

    def count_lower_than_mid(self, matrix, n, x):
        count = 0
        i = n - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= x:
                j += 1
                count += i + 1
            else:
                i -= 1
        return count

# 410 Split Array Largest Sum
    def splitArray(self, nums: List[int], m: int) -> int:
        # range of the return value
        min_sum = max(nums)
        max_sum = max(sum(nums), min_sum)
        
        while min_sum < max_sum:
            mid = min_sum + (max_sum - min_sum)//2
            if self.checkValid(nums, mid, m):
                max_sum = mid
            else:
                min_sum = mid + 1
        return min_sum
        
    def checkValid(self, nums, mid, m):
        count = 0
        curr = 0
        for i in nums:
            curr += i
            if curr > mid:
                count += 1
                if count >= m:
                    return False
                curr = i
        return True

