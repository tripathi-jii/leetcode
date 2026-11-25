
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        # Coordinate compression
        values = {v: i for i, v in enumerate(sorted(set(nums)))}
        rank = [values[x] for x in nums]

        # Build suffix array
        sa = list(range(n))
        step = 1

        while step < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + step] if i + step < n else -1
            ))

            new_rank = [0] * n
            classes = 0

            for j in range(1, n):
                a, b = sa[j - 1], sa[j]

                if (rank[a], rank[a + step] if a + step < n else -1) != \
                   (rank[b], rank[b + step] if b + step < n else -1):
                    classes += 1

                new_rank[b] = classes

            rank = new_rank

            if classes == n - 1:
                break

            step *= 2

        # Build inverse suffix array
        pos = [0] * n
        for i, x in enumerate(sa):
            pos[x] = i

        # Kasai's LCP algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            p = pos[i]

            if p == 0:
                h = 0
                continue

            j = sa[p - 1]

            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1

            lcp[p] = h

            if h > 0:
                h -= 1

        # Find shortest unique subarray
        ans = n

        for p in range(n):
            start = sa[p]

            left_lcp = lcp[p]
            right_lcp = lcp[p + 1] if p + 1 < n else 0

            length = max(left_lcp, right_lcp) + 1

            if length <= n - start:
                ans = min(ans, length)

        return ans
