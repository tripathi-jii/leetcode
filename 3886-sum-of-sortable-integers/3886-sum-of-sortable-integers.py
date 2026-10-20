from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)

            if k == 1:
                return a[0] == b[0]

            # KMP
            pattern = b
            pi = [0] * k

            j = 0
            for i in range(1, k):
                while j > 0 and pattern[i] != pattern[j]:
                    j = pi[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1

                pi[i] = j

            j = 0

            for i in range(2 * k - 1):
                x = a[i % k]

                while j > 0 and x != pattern[j]:
                    j = pi[j - 1]

                if x == pattern[j]:
                    j += 1

                if j == k:
                    start = i - k + 1

                    if start < k:
                        return True

                    j = pi[j - 1]

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            possible = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                expected = target[start:start + k]

                if not is_rotation(block, expected):
                    possible = False
                    break

            if possible:
                ans += k

        return ans