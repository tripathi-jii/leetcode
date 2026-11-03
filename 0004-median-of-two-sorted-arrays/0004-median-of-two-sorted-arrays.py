from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        low, high = 0, m

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]

            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                high = partition1 - 1

            else:
                low = partition1 + 1

        return 0.0