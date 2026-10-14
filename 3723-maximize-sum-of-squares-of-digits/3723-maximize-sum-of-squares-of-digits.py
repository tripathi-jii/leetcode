
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        if sum == 0:
            return "" if num > 0 else ""

        ans = []

        for i in range(num):
            digit = min(9, sum)
            ans.append(str(digit))
            sum -= digit

        if sum > 0:
            return ""

        return "".join(ans)