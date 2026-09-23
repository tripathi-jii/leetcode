class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.split()
        rev = strs[::-1]
        sol = " ".join(rev)

        return sol