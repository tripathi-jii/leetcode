class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(ch.lower() for ch in s if ch.isalnum())

        return strs == strs[::-1]
      
        