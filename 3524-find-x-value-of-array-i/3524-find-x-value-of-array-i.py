class Solution:
    def resultArray(self, nums, k):
        result = [0] * k

        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            remainder = num % k
            new_dp[remainder] += 1

            for r in range(k):
                if dp[r] != 0:
                    new_remainder = (r * num) % k
                    new_dp[new_remainder] += dp[r]

            dp = new_dp

            for r in range(k):
                result[r] += dp[r]

        return result