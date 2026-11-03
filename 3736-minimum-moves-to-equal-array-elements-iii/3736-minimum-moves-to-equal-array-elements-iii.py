from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)
        return sum(maximum - num for num in nums)