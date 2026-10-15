
class Solution:
    def sumCounts(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):
                seen.add(nums[j])
                count = len(seen)
                ans += count * count

        return ans
