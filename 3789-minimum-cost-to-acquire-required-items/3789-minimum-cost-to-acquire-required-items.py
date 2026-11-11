class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        separate = need1 * cost1 + need2 * cost2

        both = min(need1, need2) * costBoth

        remaining1 = max(0, need1 - need2)
        remaining2 = max(0, need2 - need1)

        both += remaining1 * cost1 + remaining2 * cost2

        all_both = max(need1, need2) * costBoth

        return min(separate, both, all_both)