from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        if n < x * k:
            return -1

        vals = sorted(set(nums))
        m = len(vals)
        mp = {v: i + 1 for i, v in enumerate(vals)}
        a = [mp[v] for v in nums]

        class BIT:
            def __init__(self, n):
                self.n = n
                self.f = [0] * (n + 1)
                self.s = [0] * (n + 1)

            def add(self, i, count, total):
                while i <= self.n:
                    self.f[i] += count
                    self.s[i] += total
                    i += i & -i

            def query(self, i):
                c = 0
                sm = 0
                while i:
                    c += self.f[i]
                    sm += self.s[i]
                    i -= i & -i
                return c, sm

            def kth(self, k):
                idx = 0
                bit = 1 << (self.n.bit_length() - 1)
                while bit:
                    nxt = idx + bit
                    if nxt <= self.n and self.f[nxt] < k:
                        idx = nxt
                        k -= self.f[nxt]
                    bit >>= 1
                return idx + 1

        bit = BIT(m)
        costs = [0] * (n - x + 1)

        for i in range(n):
            bit.add(a[i], 1, nums[i])

            if i >= x:
                bit.add(a[i - x], -1, -nums[i - x])

            if i >= x - 1:
                mid_idx = bit.kth((x + 1) // 2)
                median = vals[mid_idx - 1]

                lc, ls = bit.query(mid_idx)
                tc, ts = bit.query(m)

                costs[i - x + 1] = (
                    median * lc - ls
                    + (ts - ls) - median * (tc - lc)
                )

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            start = j * x

            for i in range(start, n + 1):
                curr[i] = curr[i - 1]
                curr[i] = min(
                    curr[i],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]