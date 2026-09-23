class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = s.split()
        sol = strs[-1]

        return len(sol)
        