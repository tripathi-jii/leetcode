class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        total = 0

        for i in range(len(s)):
            current = values[s[i]]
            if i + 1 < len(s) and current < values[s[i + 1]]:
                total -= current
            else:
                total += current
        return total
        