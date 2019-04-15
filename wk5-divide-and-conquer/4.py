class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        l1, l2 = len(nums1), len(nums2)
        start, end, half_len = 0, l1, (l1 + l2 + 1) // 2

        while start <= end:
            p1 = (start + end) // 2
            p2 = half_len - p1

            if p1 > 0 and nums1[p1 - 1] > nums2[p2]:
                end = p1 - 1
            elif p1 < l1 and nums1[p1] < nums2[p2 - 1]:
                start = p1 + 1
            else:
                if p1 == 0:
                    left = nums2[p2 - 1]
                elif p2 == 0:
                    left = nums1[p1 - 1]
                else:
                    left = max(nums1[p1 - 1], nums2[p2 - 1])

                if (l1 + l2) % 2 == 1:
                    return left

                if p1 == l1:
                    right = nums2[p2]
                elif p2 == l2:
                    right = nums1[p1]
                else:
                    right = min(nums1[p1], nums2[p2])

                return (left + right) / 2
