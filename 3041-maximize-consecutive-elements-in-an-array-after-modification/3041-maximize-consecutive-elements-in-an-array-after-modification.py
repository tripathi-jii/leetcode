
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = {}
        ans = 0

        for x in nums:
            new_dp = {}

            new_dp[x] = max(
                dp.get(x - 1, 0) + 1,
                1
            )

            new_dp[x + 1] = max(
                dp.get(x, 0) + 1,
                1
            )

            for val, length in new_dp.items():
                dp[val] = max(dp.get(val, 0), length)
                ans = max(ans, dp[val])

        return ans