from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1

        for i, num in enumerate(nums):
            if i != num:
                ans &= num

        return max(ans, 0)