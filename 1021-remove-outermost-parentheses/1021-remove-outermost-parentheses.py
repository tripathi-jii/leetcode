class Solution:
    def removeOuterParentheses(self, s):
        result = ""
        balance = 0

        for ch in s:
            if ch == "(":
                if balance > 0:
                    result += ch
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    result += ch

        return result