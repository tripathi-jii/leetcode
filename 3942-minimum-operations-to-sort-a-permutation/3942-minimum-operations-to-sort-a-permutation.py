from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def check(arr, reversed_once):
            k = arr.index(0)

            for i in range(n):
                if arr[i] != (i - k) % n:
                    return -1

            if reversed_once:
                return 1 + min(k, n - k)

            return min(k, n - k + 2)

        ans1 = check(nums, False)
        ans2 = check(nums[::-1], True)

        valid = [x for x in (ans1, ans2) if x != -1]
        return min(valid) if valid else -1