# 23. Merge K Sorted Arrays
    def merge2Lists(self, l1, l2):
        dummy_head = ListNode(None)
        curr = dummy_head
        p1, p2 = l1, l2
        while p1 or p2:
            if p1 and (not p2 or p1.val < p2.val):
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        return dummy_head.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) <= 1:
            return None if len(lists) == 0 else lists[0]
        
        n = len(lists)
        gap = 1
        while gap < n:
            print(gap)
            for i in range(0, n - gap - 1, 2*gap):
                lists[i] = self.merge2Lists(lists[i], lists[i + gap])
            gap *= 2
        return lists[0]

# 43. Multiply Strings
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # the solution the interviewer might like
        if num1 == '0' or num2 == '0':
            return '0'
        ans = 0
        mapDict = {chr(ord('0') + i): i for i in range(10)}
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = mapDict[n1] * mapDict[n2]    
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10 ** j)
                pre = first
            curr += pre * (10 ** len(num1))
            ans += curr * 10 ** i
        return str(ans)
        # my solution
        return str(int(num1) * int(num2))

# 4. Median of Two Sorted Arrays
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return self.getKth(nums1, nums2, (m + n) // 2 + 1)
        else:
            return 0.5 * (self.getKth(nums1, nums2, (m + n) // 2) + self.getKth(nums1, nums2, (m + n) // 2 + 1))
        
    def getKth(self, nums1, nums2, k):
        print(nums1, nums2, k)
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.getKth(nums2, nums1, k)
        if m == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p1 = min(k//2, m)
        p2 = k - p1
        if nums1[p1 - 1] <= nums2[p2 - 1]:
            return self.getKth(nums1[p1:], nums2, p2)
        else:
            return self.getKth(nums1, nums2[p2:], p1)

# 215. Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using heap
        # form a heap
        import heapq
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]

# 240. Search a 2D Matrix II
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # my solution
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        def searchSubMatrix(matrix, left, right, target):
            """
            left: the i, j tuple of the top left item
            right: the i, j tuple of the bottom right item
            """
            print(left, right)
            if left[0] > right[0] or left[1] > right[1]:
                return False
            if left == right and matrix[left[0]][left[1]] != target:
                return False
            
            mid = (left[0] + right[0])//2, (left[1] + right[1])//2
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] > target:
                return searchSubMatrix(matrix, left, mid, target) or \
                       searchSubMatrix(matrix, (left[0], mid[1] + 1), (mid[0], right[1]), target) or \
                       searchSubMatrix(matrix, (mid[0] + 1, left[1]), (right[0], mid[1] - 1), target)
            else:
                return searchSubMatrix(matrix, (left[0], mid[1] + 1), right, target) or \
                       searchSubMatrix(matrix, (mid[0] + 1, left[1]), (right[0], mid[1]), target)
        
        return searchSubMatrix(matrix, (0, 0), (m - 1, n - 1), target)
        #########
        # quicker
        #########
        if not matrix or not matrix[0]: return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j > -1:
            if matrix[i][j] == target: return True
            if target < matrix[i][j]: j -= 1 # rule out the whole column
            else: i += 1 # rule out the whole row
        return False


# 932. Beautiful Array
    def beautifulArray(self, N):
        res = [1]
        while len(res) < N:
            res = [2 * i - 1 for i in res] + [2 * i  for i in res]
        return [i for i in res if i <= N]
